======================
Sphinx docs template
======================
使用sphinx编写文档的模板项目。

* 支持 `markdown` 和 `reStructuredText` 。
* 支持生成中文pdf。
* 安装了一些不错的主题。

依赖
======

#. 中文pdf依赖： `apt install latex-cjk-all` || `pacman -Sy texlive texlive-lang`
#. `mermaid` 命令： `yarn global add  @mermaid-js/mermaid-cli`
#. `Python` 依赖（shinx插件和一些主题） ::

    pip install -r requirements.txt
