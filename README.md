[日本語](#日本語) | [English](#english)

#### english

# Comfy UI Text List Product

This is a custom node for Comfy UI.

It mainly wraps `itertools.product` and can be used to create patterns by combining prompts.

It is recommended to install this custom node in combination with the nodes from the [WAS Node Suite](https://github.com/WASasquatch/was-node-suite-comfyui).

![ProductedString](<doc/スクリーンショット 2024-06-17 000135.png>)

In the screenshot above, `[1girl, 1boy]` and `[blonde_hair, crown]` and `[beach, futuristic City]` are combined to create an 8-line (2 * 2 * 2) multiline string.

Additionally, by connecting to the WAS Node Suite's Text Load Line From File and specifying 8 in Comfy UI's Queue Prompt, you can generate 8 patterns.

## Installation

Open the ComfyUI Manager, click on `Install via Git URL`, enter `https://github.com/opvelll/ComfyUI_TextListProduct`, and press OK.


## Nodes

### TextListProduct

![TextListProduct](<doc/スクリーンショット 2024-06-21 145008.png>)

This is a basic node. `TextListProduct` combines two lists and creates a new list joined by the specified separator.

It is intended to be used in combination with the WAS Node Suite nodes like Text List to Text, Save Text File, and Text Load Line From File.

#### TextListProductWithSingleA TextListProductWithSingleB TextListProductWithSingleBoth

These nodes are shorthand nodes for when you want to use single words from one or both lists.

In other words, it is equivalent to passing an empty string at the beginning of the list passed to TextListProduct.

![TextListProductWithSingleB](<doc/スクリーンショット 2024-06-21 151730.png>)

### ProductedString

![ProductedString](<doc/スクリーンショット 2024-06-17 000135.png>)

This is a further shorthand node for TextListProduct. It combines multiple lists and returns a multiline string with line breaks.

## Usage Examples

You can use it to add a specified string at the beginning of the strings in the list.

Combine expression patterns * pose patterns * camera work patterns * ... and use the Save Text File node from the WAS Node Suite to generate a text file.

## License

MIT


#### 日本語
# Comfy UI Text List Product

Comfy UI のカスタムノードです。

主にitertools.productをラップしたもので、プロンプトをかけ合わせてパターンを作ることに利用できます。

[WAS Node Suite](https://github.com/WASasquatch/was-node-suite-comfyui)のノードと組み合わせることを想定しているので、こちらのカスタムノードもインストールすることを推奨します。

![ProductedString](<doc/スクリーンショット 2024-06-17 000135.png>)

上のスクリーンショットでは、`[ 1girl, 1boy ]` と `[ blonde_hair, crown ]` と `[ beach, futuristic City ]` を掛け合わせて、8行(2 * 2 * 2)のマルチライン文字列を作っている様子です。

あとは、WAS Node SuiteのText Load Line From Fileにつなげて、Comfy UIのQueue Promptに8を指定すると8パターンが生成されます。

## インストール

ComfyUI Managerを開いて、`Install via Git URL`をクリック、`https://github.com/opvelll/ComfyUI_TextListProduct`と入力してOKを押します。


## ノード

### TextListProduct

![TextListProduct](<doc/スクリーンショット 2024-06-21 145008.png>)

基本的なノード。`TextListProduct` は、2つのリストを掛け合わせて、指定されたセパレータで結合した新しいリストを作成します。

WAS Node SuiteのText List to Text、Save Text File、TextLoad Line From File等と組み合わせて使うのを想定しています。

#### TextListProductWithSingleA TextListProductWithSingleB TextListProductWithSingleBoth

これらのノードは、片方、または両方のリストの単語単体を使いたいときのショートハンド用ノードです。

つまりTextListProductに渡すリストの先頭に空文字を渡した時と同じです。

![TextListProductWithSingleB](<doc/スクリーンショット 2024-06-21 151730.png>)

### ProductedString

![ProductedString](<doc/スクリーンショット 2024-06-17 000135.png>)

さらにTextListProductのショートハンドノードです。複数のリストを掛け合わせて、改行を加えて複数行の文字列にして返します。

## 使用例

リストの文字列の先頭に指定の文字列を加えたいとか。

表情パターン * ポーズパターン * カメラワークパターン * ... と組み合わせて、WAS Node SuiteのSave Text Fileノードを使って、文字列ファイルを生成するとか。

## License

MIT