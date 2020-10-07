const IGNORE_FILES = [
  /* gitignore style */
  'SUMMARY.md',
];
const DEFAULT_README_TITLE = 'Introduction';

////////////////////////////////////////////////
const fs = require('fs');
const path = require('path');

const isNotIgnored = (() => {
  const ignoredPatterns = fs.readFileSync('./.gitignore', 'utf8')
    .split('\n')
    .map(f => f.trim())
    .filter(f => f.length > 0)
    .filter(f => f[0] !== '#')
    .concat(IGNORE_FILES)
    .map(f => new RegExp(f.replace(/\*/g, '(.*?)')));

  return (f) => {
    if(!(f instanceof File)) throw "Error: expecting File";
    return ignoredPatterns.reduce((bool, p) => bool && !p.test(f.path, true));
  };
})();

const indent = (s, n=4) => {
  const spaces = (new Array(n + 1)).join(' ');
  return spaces + s.replace(/\n/g, '\n' + spaces);
};

class File{
  constructor(path){
    this.path = path;
  }

  get filename(){
    return this.path.substring(this.path.lastIndexOf('/') + 1);
  }

  get name(){
    const p = this.filename;
    if(p.lastIndexOf('.') === -1) return p;
    return p.substring(0, p.lastIndexOf('.'));
  }

  get prettyname(){
    const capitalize = (s) => {
      if(s.length === 0) return '';
      return [s[0].toUpperCase(), ...s.substring(1).toLowerCase()].join('');
    };
    const sepWords = (p) => p.replace(/[-_]/g, ' ');
    return capitalize(sepWords(this.name));
  }

  get ext(){
    return this.path.substring(this.path.lastIndexOf('.'));
  }

}

class Dir extends File{
  ls(){
    const isVisible = (f) => f[0] !== '.';

    return fs.readdirSync(this.path)
      .filter(isVisible)
      .map((f) => path.join(this.path, f))
      .map(p => new (fs.statSync(p).isDirectory()? Dir: File)(p));
  }

  lsdirs(){
    return this.ls().filter(f => f instanceof Dir);
  }
}

class Root extends Dir{
  /* directories are viewed as Parts
   * files are Articles */
  ls(){
    return super.ls()
      .filter(isNotIgnored)
      .map(f => new (f instanceof Dir? Part: Article)(f.path))
      .filter(f => f instanceof Article? f.ext === '.md': f);
  }

  getHeader(){
    return `# Summary`;
  }

  articlesSummary(){
    return this.ls()
      .filter(f => f instanceof Article)
      .map(f => f.toSummary())
      .join('\n');
  }

  directoriesSummary(){
    return this.lsdirs()
      .map(part => part.toSummary())
      .join('\n');
  }

  getSummary(){
    const artSum = this.articlesSummary()
    const dirsSum = this.directoriesSummary();
    return [artSum, dirsSum].filter(s => s.trim() !== '').join('\n\n');
  }

  toSummary(){
    return this.getHeader() + '\n' + this.getSummary() + '\n';
  }
}

class Part extends Root{
  /* directories are viewed as Chapters
   * files are Articles */
  ls(){
    return super.ls()
      .map(f => f instanceof Part? new Chapter(f.path): f)
  }

  getHeader(){
    return `## ${this.prettyname}`;
  }
}

class Chapter extends Part{
  ls(){
    return super.ls().filter(f => f.filename !== 'README.md');
  }

  getHeader(){
    const readme_path = path.join(this.path, 'README.md');
    return `* [${this.prettyname}](${readme_path})`
  }

  getSummary(){
    return indent(super.getSummary());
  }
}

class Article extends File{
  get prettyname(){
    const original_prettyname = super.prettyname;
    if(original_prettyname !== 'Readme') return original_prettyname;
    return DEFAULT_README_TITLE;
  }

  toSummary(){
    return `* [${this.prettyname}](${this.path})`;
  }
}

const summary = new Root('.').toSummary();

fs.writeFileSync('SUMMARY.md', summary);
