# AI-Lab 
## 学习计划与进度

|学习计划|学习进度|
|--|--|
|第一周|环境配置|配置所需要的环境|
|第二周|掌握linux以及基本的命令行操作和git,github的基本使用方法|已完成|
|第三周|学习python的基本语法和数据类型|并且练习相关的python代码|
|第四周| 学习如何下载conda环境 以及docker的初步了解

报错详情：在配置 AI 协同插件（TraeCode Plugin）时，遇到了“认证错误，请重新登录后重试”的报错。



外部参考文档：
 · VSCode 官方文档（https://code.visualstudio.com/）
 · Markdown 语法规范指南

```python
print("Hello, World!")
for i in range(10):
    print(i)

```

技术摘记

    1. 学习了python的基本语法和数据类型，以及相关的python代码。
    2. 学习了linux以及基本的命令行操作和git,github的基本使用方法。
    3. 了解了conda环境以及docker的基本概念和使用方法。
    4. 学习了VSCode的基本使用方法。   
   
  ## task03task04 操作命令的截图
  ### linux 执行历史记录的截图
 
  [linux 执行历史记录的截图]
     ![alt text](linux执行历史记录截图.png)
### git 操作命令的截图
  ![git 执行历史记录的截图]
![alt text](git的操作截图.png)


![alt text](git操作截图.png)


### git的操作命令笔记
* 分支管理
  * 创建分支  
       ```  
       git checkout -b 分支名(git checkout命令加上-b参数表示创建并切换，否则只是切换分支)
       ### 相当于以下两条命令
       git branch 分支名(创建分支)
       git checkout 分支名（切换分支）
       ``` 
  * 查看分支  
     ```
     git branch
     ```
  * 切换分支
     ```
     git checkout 分支名
     ```
  * 合并分支
     ```
     git merge 分支名  (合并指定分支到当前分支)
     ```
  * 删除分支
     ```
     git branch -d 分支名  (删除指定分支)
     ```

     ![alt text](d8cf0f07cb73dc4fcbf349765d469310.png)

* 提交管理
  * 提交文件
     ```
     git add 文件名  (添加指定文件到暂存区)
     ```
  * 提交暂存区文件
     ```
     git commit -m "提交信息"  (提交暂存区文件到当前分支)
     ```
  * 查看提交记录
     ```
     git log
     ```
  * 查看提交详情
     ```
     git show 提交哈希值  (查看指定提交的详细信息)
     ```
* 解决冲突（Git用<<<<<<<，=======，>>>>>>>标记出不同分支的内容）
  * 手动解决冲突
     ```
     git add 文件名  (添加解决冲突后的文件到暂存区)
     ```
  * 提交解决冲突后的文件
     ```
     git commit -m "解决冲突"  (提交解决冲突后的文件到当前分支)
     ```

     ![alt text](8509ef2acc596e5c471e978d5e1bed86.png)


     ![alt text](f9194958c4b6381a371d8748d5b788ee.png)

* Feature 分支(创建合并删除)

          
      
     ![alt text](44fb993c6763dacf40c95ebce38b5673-2.png)

      
## docker 源码镜像容器的截图

<img width="1950" height="1127" alt="6cb2acc9b9faec4b683dd5ccee33221e" src="https://github.com/user-attachments/assets/4b7be058-7f37-44a8-9781-a9a0934f4b28" />

<img width="1470" height="783" alt="9fe10d2d1ddcd5db55223d3e204b5b09" src="https://github.com/user-attachments/assets/07d8ab68-500f-4367-b636-0cfdc1e4b171" />




