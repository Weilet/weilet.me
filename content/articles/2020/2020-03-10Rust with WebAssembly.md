Title: Rust with WebAssembly
Date: 2020-03-10 5:09
Author: Weilet
Category: Tech
Tags: Rust, wasm
Slug: Rust with WebAssembly
Status: published



> 大人，时代变了



### About wasm

WebAssembly ，亦称 wasm ，是一种基于浏览器的虚拟机的代码。由于它是二进制的，因此机器能够较快的执行。wasm 目前不能直接编写，它可以由 C/C++/Rust 生成。目前，Chrome 、 Microsoft Edge 、 Firefox 、 Safari 支持 wasm。



### Why Rust?

俺在学习 Rust ，Rust 是一门写起来很愉快的语言。



### 准备

#### 安装Rust

[Rust官网](https://www.rust-lang.org/zh-CN/tools/install)

#### 安装wasm-pack

[Rustwasm官网](https://rustwasm.github.io/wasm-pack/installer/)



### 流程

新建项目

```
cargo new wasm
```

目录结构

```
.
├── Cargo.toml
└── src
    └── lib.rs
```

添加依赖

```toml
[dependencies]
wasm-bindgen = "0.2.48"
```

update一下

```
cargo update
```

编写Rust代码

```rust
// lib.rs
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn fibonacci(n: u32) -> u32 {
    match n {
        0 => 1,
        1 => 1,
        _ => fibonacci(n - 1) + fibonacci(n - 2),
    }
}
```

编译Rust代码为WebAssembly

```
wasm-pack build --no-typescript --target web --mode normal   
```

生成在pkg目录

目录结构

```
.
├── wasm.js
└── wasm_bg.wasm
```

编写html文件调用wasm

```html
<script type="module">
  main()

  async function main() {
    const wasm = await import('/pkg/wasm.js')
    
    await wasm.default('/pkg/wasm_bg.wasm')

    console.log(wasm.fibonacci(40))
  }
</script>
```

如果成功，你将在Chrome的console中看到答案。



### Why wasm faster?

可参考：

[mozilla官网介绍](https://developer.mozilla.org/zh-CN/docs/WebAssembly/Concepts#WebAssembly%E6%98%AF%E4%BB%80%E4%B9%88%EF%BC%9F)

[Tom’s zone博客]([https://hasaki.xyz/blog/2019-07-20-%E4%BD%BF%E7%94%A8-rust-%E7%BC%96%E5%86%99-webassembly-/](https://hasaki.xyz/blog/2019-07-20-使用-rust-编写-webassembly-/))











