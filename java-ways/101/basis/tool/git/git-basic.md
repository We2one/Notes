```yaml
   Author: Gentleman.Hu
   Create Time: 2020-09-19 20:20:08
   Modified by: Gentleman.Hu
   Modified time: 2020-09-25 19:15:41
   Email: justfeelingme@gmail.com
   Home: https://crushing.xyz
   Description:
 ```

## Git some notes

### 1. git存储方式

- 按照元数据内部存储类似k/v存储

  ```shell
  git hash-object -w "filename" #查看hash
  ```

  ![image-20200720190551457](https://cdn.jsdelivr.net/gh/gentlemanhu/public-store/images/image-20200720190551457.png)

- 基本使用

  ```shell
  git add -A ;#添加所有
  git commit -am "meg";#提交到本地仓库
  git rm --cached target -r(recursion);#删除暂存区的文件（add后的文件）
  git push;#提交到远程仓库
  git branch -d {dev};#删除分支
  git checkoout <branch name>;#切换分支
  git merge <merge target>;#合并分支。若有冲突，则需要手动修改再commit 
  git log ;
  ```

  ![image-20200720193811323](https://cdn.jsdelivr.net/gh/gentlemanhu/public-store/images/image-20200720193811323.png)

- 几种创建分支

  - 基于当前分支新建分支

    > git branch <branch name>

  - 基于提交新建分支

    > git branch <branch name> <commit id>

  - 基于tag新建分支

    > git branch <branch name> <tag name>
  
  - 其他待实际操作发现
  
---

## 一些问题

- ` git commit -a`和`git add .`区别

  - `git commit -a` means almost[*] the same thing as `git add -u && git commit`.

  - It's not the same as `git add .` as this would add untracked files that aren't being ignored, `git add -u` only stages changes (including deletions) to already tracked files.

  - [*] There's a subtle difference if you're not at the root directory of your repository. `git add -u` stages updates to files in the current directory and below, it's equivalent to `git add -u .` whereas `git commit -a` stages and commits changes to *all* tracked files.

	>  source:[区别](https://stackoverflow.com/questions/3541647/git-add-vs-git-commit-a)

- `git add -A` and `git add .` and `git add -u` 区别
  - **According to git version 1.x**

	  “**git add -A**” is equivalent to “**git add .**” and “**git add -u**“
	
	  - **git add -A** stages All
	  - **git add .** stages new and modified, without deleted
	  - **git add -u** stages modified and deleted, without new
	
	  The important point about **git add .** is that it looks at the working tree and adds all those paths to the staged changes if they are either changed or are new and not ignored, it does not stage any ‘rm’ actions.
	
	  **git add -u** looks at all the already tracked files and stages the changes to those files if they are different or if they have been removed. It does not add any new files, it only stages changes to already tracked files.
	
	  **git add -A** is a handy shortcut for doing both.
	
	  - **git add -A is equivalent to git add –all**
	  - **git add -u is equivalent to git add –update**
	
	- **According to git version 2.x**
	
	  - **git add -A** stages All
	  - **git add .** stages All in same path
	  - **git add -u** stages modified and deleted, without new
	
	  There is no more difference in **2.0**. **git add .** equals to **git add -A** for the same path, the only difference is if there are new files in other paths of the tree.
	
	  With **Git 2.0**, **git add -A** is **default**: **git add .** equals **git add -A .**
	
	> Source:[differences]([https://www.dineshonjava.com/difference-between-git-add-a-and-git-add-dot-and-git-u/#:~:text=git%20add%20%2Du%20looks%20at,handy%20shortcut%20for%20doing%20both.](https://www.dineshonjava.com/difference-between-git-add-a-and-git-add-dot-and-git-u/#:~:text=git add -u looks at,handy shortcut for doing both.))
	>
	> [`git add .`and `git add -u`](https://stackoverflow.com/a/2190440)

- git 如何处理Symlink file，如何处理链接的文件？

  - 只是记录追踪了合格链接文件，并未追踪这个链接引用的文件

    <span style="color:blue">So, that's what Git does to a symbolic link: when you git checkout the symbolic link, you either get a text file with a reference to a full filesystem path, or a symlink, depending on configuration. **The data referenced by the symlink is not stored in the repository.**</span>

  > [how works](https://stackoverflow.com/a/46510347)

  - 建议写成相对路径添加e.g.`ln -s ../xxx.md xxx.md`

    ```bash
    # Not good for Git repositories
    ln -s /Users/gio/repo/foo.md ./bar/foo.md
    
    # Good for Git repositories
    cd ./bar && ln -s ../foo.md foo.md
    ```
  <span style="color:blue">The reason for this is that given that a symlink contains the path to the referenced file, if the path is relative to a specific machine the link won't work on others. If it's relative to the repository itself on the other hand, the OS will always be able to find the source.</span>
  > [Source](https://www.mokacoding.com/blog/symliks-in-git/)

[^ justGo]:Way to my success!

