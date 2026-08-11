[日本語](#日本語) | [English](#english)

#### english

# Comfy UI Text List Product

This is a custom node for Comfy UI.

It creates prompt patterns by calculating cartesian products and concatenating text lists.

Results can be output in different forms depending on the intended use:

- `TextListProduct`: A `LIST` that can be passed to other list-processing nodes
- `Producted String`: Both a multiline `STRING` and the same combinations as a `LIST`
- `Text List to Sequence`: Sequential `STRING` values that run downstream nodes once per item

![ProductedString](doc/producted-string.png)

In the screenshot above, three Text List nodes supply `[1girl, 1boy]`, `[blonde_hair, crown]`, and `[beach, futuristic City]`. `Producted String` combines them into an 8-line (2 * 2 * 2) multiline string.

## Installation

It can be installed via Install Custom Nodes in the [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager)


## Nodes

### ・ MultilineStringToList

Creates a Python `list[str]` from a multiline string, with one item per line, and returns it through a `LIST` socket. This `LIST` travels through the workflow as one value.

- `trim_whitespace` removes whitespace around each line. It is enabled by default.
- `keep_empty_lines` preserves empty lines as empty string items. It is disabled by default.
- Empty input returns an empty list, and comment-like lines are kept as normal text.

For example, entering `red`, `green`, and `blue` on separate lines produces `["red", "green", "blue"]`.

### ・ StringsToList

Collects up to seven connected string inputs (`text_a` through `text_g`) into one Python `list[str]` in input order and returns it through a `LIST` socket. Unconnected inputs are skipped, while connected empty strings are preserved.

Compatible `LIST` outputs from other custom nodes, including WAS Node Suite, can also be connected to this package's LIST inputs.

### ・ TextListToSequence

Converts a Python text `LIST` into ComfyUI's sequential `STRING` output. Downstream nodes that normally accept one string are executed once for each list item.

The input must contain at least one item, and every item must be a string. Empty string items are valid and cause one downstream execution with an empty string. An empty list raises a clear error because ComfyUI cannot safely process an empty sequential list.

For sequential prompt generation, connect nodes as follows:

`TextListProduct → Text List to Sequence → CLIP Text Encode`

### ・ TextListProduct

![TextListProduct](doc/text-list-product.png)

This is a basic node. `TextListProduct` combines two lists and returns the results as a new `LIST`, joined by the specified separator.

`max_results` can be used to stop generation early when the cartesian product would become too large. `0` means unlimited.

### ・ TextListProductWithSingleA 
### ・ TextListProductWithSingleB
### ・ TextListProductWithSingleBoth

These nodes are shorthand nodes for when you want to use single words from one or both lists.

In other words, it is equivalent to passing an empty string at the beginning of the list passed to TextListProduct.

These nodes also support `max_results` to cap the number of generated combinations.

![TextListProductWithSingleB](doc/text-list-product-with-single-b.png)

### ・ ProductedString

![ProductedString](doc/producted-string.png)

Combines multiple lists and returns every combination in two forms: one newline-delimited `STRING` for display or saving, and one `LIST` for further list processing. Both outputs contain the same combinations in the same order.

`newline_char` affects only the `STRING` output. `max_results` caps both outputs to the same number of combinations.

### ・ PromptPairConcat

![PromptPairConcat](doc/workflow_prompt_pair_concat.png)

Takes two prompt lists, combines each corresponding pair with the specified separator, and returns the results as a `LIST`.

`isClean` trims whitespace and removes duplicated separators inside each item before concatenation.

`trailing_separator` optionally appends the separator to the end of each output string for prompt-building workflows.


## Usage Examples

- Convert expression, pose, and camera-work patterns with `Multiline String to List`, then combine them with `Producted String` to output every combination as multiline text.
- Add a fixed prefix to every string in a list.
- Connect the `LIST` output from `Producted String` through `Text List to Sequence` to `CLIP Text Encode` or another regular string input for sequential generation.
- Connect the multiline `STRING` from `Producted String` to a node such as Save Text File to save it externally.

## License

MIT


#### 日本語
# Comfy UI Text List Product

Comfy UI のカスタムノードです。

主にプロンプトのリストの積や連結を行い、複数のプロンプトのパターンを作ることができます。

処理結果は、用途に応じて次の形式で出力できます。

- `TextListProduct`：ほかのLIST処理へ渡せる `LIST`
- `Producted String`：複数行の `STRING` と、同じ組み合わせを格納した `LIST`
- `Text List to Sequence`：各要素を後段で1件ずつ処理するための逐次 `STRING`

![ProductedString](doc/producted-string.png)

上のスクリーンショットでは、3つのText Listノードから `[1girl, 1boy]`、`[blonde_hair, crown]`、`[beach, futuristic City]` を受け取り、`Producted String` で8行（2 * 2 * 2）のマルチライン文字列を作っています。

## インストール

[ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager)のInstall Custom Nodesからインストールできます。


## ノード

### ・ MultilineStringToList

複数行の文字列から、1行につき1要素のPython `list[str]` を作成し、`LIST` ソケットから出力します。この `LIST` は、ワークフロー内では1つの値として扱われます。

- `trim_whitespace` は各行の前後空白を除去します。既定で有効です。
- `keep_empty_lines` は空行を空文字列の要素として保持します。既定では無効です。
- 入力が空なら空LISTを返し、コメントのように見える行も通常の文字列として保持します。

たとえば、`red`、`green`、`blue` を別々の行に入力すると、`["red", "green", "blue"]` を返します。

### ・ StringsToList

別々のノードから受け取った最大7個の文字列入力（`text_a`～`text_g`）を、入力順に1つのPython `list[str]` へまとめ、`LIST` ソケットから出力します。未接続の入力は無視し、接続された空文字列は保持します。

なお、同じ `LIST` 型を出力するWAS Node Suiteなどのノードも、このパッケージのLIST入力へ接続できます。

### ・ TextListToSequence

Pythonのテキスト `LIST` を、ComfyUI標準の逐次処理用 `STRING` 出力へ変換します。通常は1つの文字列を受け取る後段ノードが、LISTの各要素について1回ずつ実行されます。

入力には1つ以上の要素が必要で、すべて文字列でなければなりません。空文字列の要素は有効で、後段を空文字列で1回実行します。空LISTはComfyUIが安全に処理できないため、分かりやすいエラーを返します。

プロンプトを逐次処理する場合は、次のように接続します。

`TextListProduct → Text List to Sequence → CLIP Text Encode`

### ・ TextListProduct

![TextListProduct](doc/text-list-product.png)

基本的なノード。`TextListProduct` は、2つのリストを掛け合わせ、指定されたセパレータで結合した結果を新しい `LIST` として出力します。

`max_results` を使うと、組み合わせ数が大きくなりすぎる場合でも途中で打ち切れます。`0` は無制限です。

#### ・ TextListProductWithSingleA 
#### ・ TextListProductWithSingleB 
#### ・ TextListProductWithSingleBoth

これらのノードは、片方、または両方のリストの単語単体を使いたいときのショートハンド用ノードです。

つまりTextListProductに渡すリストの先頭に空文字を渡した時と同じです。

これらのノードでも `max_results` で生成件数の上限を設定できます。

![TextListProductWithSingleB](doc/text-list-product-with-single-b.png)

### ・ ProductedString

![ProductedString](doc/producted-string.png)

複数のリストを掛け合わせ、すべての組み合わせを2つの形式で出力します。出力0は、結果全体の表示や保存に使える複数行の `STRING` です。出力1は、同じ組み合わせを同じ順序で格納した、後段のLIST処理に使える `LIST` です。

`newline_char` は `STRING` 出力だけに適用されます。`max_results` は両方の出力を同じ件数に制限します。

### ・ PromptPairConcat

![PromptPairConcat](doc/workflow_prompt_pair_concat.png)

2つのプロンプトリストを入力として受け取り、それぞれのリスト要素を指定したセパレータで結合し、`LIST` として出力します。zip関数のようなものです。

`isClean` を有効にすると、各要素の前後空白や余分なセパレータを整理してから結合します。

`trailing_separator` を有効にすると、各出力文字列の末尾にセパレータを追加できます。プロンプトを後段で継ぎ足す用途向けです。

## 使用例

- 表情、ポーズ、カメラワークの各パターンを `Multiline String to List` でLIST化し、`Producted String` で掛け合わせて、すべての組み合わせを複数行の文字列として出力できます。
- リスト内の各文字列の先頭へ、指定した文字列を付け足せます。
- `Producted String` の `LIST` 出力を、`Text List to Sequence` 経由で `CLIP Text Encode` などへ接続し、1件ずつ連続生成できます。
- `Producted String` が出力した複数行の `STRING` を、Save Text Fileなどのノードへ接続して外部ファイルに保存できます。

## Workflow

![Workflow](doc/workflow_textlistproduct.png)

この画像のText Listノードは、このパッケージの `Multiline String to List` または `Strings to List` に置き換えられます。

## License

MIT
