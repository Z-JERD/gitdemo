"""
git branch -a

    * master
       remotes/origin/HEAD -> origin/master
       remotes/origin/dev
       remotes/origin/master		

新建分支并切换到指定分支
    
	git checkout -b iss20210430 origin/dev

git checkout -b 本地分支名 origin/远程分支名

该命令可以将远程git仓库里的指定分支拉取到本地，这样就在本地新建了一个dev分支，并和指定的远程分支release/caigou_v1.0关联了起来

将本地分支推送到远程

	$ git push -u origin iss20210430:origin/dev

        git push <远程主机名> <本地分支名>:<远程分支名>

"""
