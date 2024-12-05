# [Silver V] Railroad - 24789 

[문제 링크](https://www.acmicpc.net/problem/24789) 

### 성능 요약

메모리: 31120 KB, 시간: 32 ms

### 분류

애드 혹, 그래프 이론

### 제출 일자

2024년 12월 5일 23:11:25

### 문제 설명

<p>Theta likes to play with her DUPLO railway set. The railway set she has consists of pieces of straight tracks, curved tracks, Y-shaped switches, and X-shaped level junctions, as well as bridges that allow one track to cross over another.  There are also straight tracks that are railroad crossings to allow car traffic to cross.</p>

<p>Close-ups of some of the pieces are shown below:</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/0ad8a0d0-505c-4b68-ab46-b0af36cac393/-/preview/" style="width: 200px; height: 150px;"> <img alt="" src="https://upload.acmicpc.net/6e27e13c-8257-4c11-a83f-2825a4d3d2dd/-/preview/" style="width: 200px; height: 150px;"> <img alt="" src="https://upload.acmicpc.net/86e4afa3-090d-4669-8d10-b9eca453a83f/-/preview/" style="width: 200px; height: 150px;"></p>

<p>To play, she picks a number of X-shaped level junctions and a number of Y-shaped switches and connects them with straight and curved pieces, using bridges as necessary.</p>

<p>Because the set doesn't include any bumpers, she wants to build a closed track, like all the examples shown in the manual that came with the set:</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/259ef401-f156-4f8b-a7c1-bc37cb488205/-/preview/"></p>

<p style="text-align: center;">Figure 1: Various track layouts possible with the DUPLO railway system. Curved pieces are shown in green, straights in red, switches in orange, level junctions in yellow, bridges in blue, and crossings in black. DUPLO is a trademark of the LEGO Group.</p>

<p>Unfortunately, sometimes, this doesn't seem to work with the number of X-shaped level junctions and Y-shaped switches she starts out with.</p>

<p>She quickly figures out exactly when it is possible to build a closed track - can you figure it out, too?</p>

<p>Write a program that outputs if it is possible to build a railroad that does not require any bumpers (i.e., which does not have any dead-end tracks).</p>

### 입력 

 <p>The input consists of a single test case with two integer numbers <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44B TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>X</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$X$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D44B TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>X</mi><mo>≤</mo><mn>1000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0 \le X \le 1000$</span></mjx-container>) and <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D44C TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$Y$</span></mjx-container> (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D44C TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>0</mn><mo>≤</mo><mi>Y</mi><mo>≤</mo><mn>1000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$0 \le Y \le 1000$</span></mjx-container>) denoting the number of level junctions and switches, respectively. You may assume that Theta has sufficiently many straight and curved pieces as well as bridges.</p>

### 출력 

 <p>Output <code>possible</code> if she can build a closed track using all level junctions and all switches without any dead ends, or <code>impossible</code> otherwise.</p>

