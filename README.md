
<h1 align='center'>getpdf</h1>
<p align='center'>

<br/>
<a href="https://github.com/perseu912"><img title="Autor" src="https://img.shields.io/badge/Autor-reinan_br-blue.svg?style=for-the-badge&logo=github"></a>
<br/>
<p align='center'>
<!-- github dados -->
<!-- sites de pacotes -->
<a href='https://pypi.org/project/noaawc/'><img src='https://img.shields.io/pypi/v/getpdf'></a>
<a href='#'><img src='https://img.shields.io/pypi/wheel/getpdf'></a>
<a href='#'><img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/getpdf"></a>
<img alt="PyPI - License" src="https://img.shields.io/pypi/l/getpdf">
<br/>


<img src='https://img.shields.io/badge/system-linux%20%7C%20deb-brightgreen'>

<img alt="GitHub Pipenv locked Python version" src="https://img.shields.io/github/pipenv/locked/python-version/perseu912/getpdf">

<br/>
<!-- outros premios e analises -->
<!-- <a href='#'><img alt="CodeFactor Grade" src="https://img.shields.io/codefactor/grade/github/perseu912/noawclg?logo=codefactor">
</a> -->
<!-- redes sociais -->
<a href='https://instagram.com/gpftc_ifsertao/'><img src='https://shields.io/badge/insta-gpftc_ifsertao-darkviolet?logo=instagram&style=flat'></a>
<a href='https://discord.gg/pFZP86gvEm'><img src='https://img.shields.io/discord/856582838467952680.svg?label=discord&logo=discord'></a>

</p>
</p>
<p align='center'> <b>Library for getting pdf's from Google search's</b></p>
<hr/>

## Instalation

```sh
$ pip3 install getpdf -U
```

## Examples

```sh
$ getpdf 'waves gravtational' 12
```

results

```sh
size search 12
 [1/12] [0min:0sec | ETA: 0min:1sec] 
pdf/waves_gravtational/lec005.pdf 0.15 MB saved! [ping: 26.0 ms] 

 [2/12] [0min:3sec | ETA: 0min:12sec] 
pdf/waves_gravtational/ssi94-002.pdf 0.52 MB saved! [ping: 352.3 ms] 

 [3/12] [0min:9sec | ETA: 0min:20sec] 
pdf/waves_gravtational/1710.04635.pdf 0.94 MB saved! [ping: 532.8 ms] 

 [4/12] [0min:10sec | ETA: 0min:16sec] 
pdf/waves_gravtational/cursoGW-ICTP-Sturani1.pdf 0.67 MB saved! [ping: 100.2 ms] 

 [5/12] [0min:12sec | ETA: 0min:14sec] 
pdf/waves_gravtational/rnoti-p684.pdf 2.44 MB saved! [ping: 232.3 ms] 

 [6/12] [0min:14sec | ETA: 0min:12sec] 
pdf/waves_gravtational/pdf.pdf 0.00 MB saved! [ping: 178.2 ms] 

 [7/12] [0min:15sec | ETA: 0min:9sec] 
pdf/waves_gravtational/annurev.nucl.54.070103.181251.pdf 1.18 MB saved! [ping: 113.8 ms] 

 [8/12] [0min:19sec | ETA: 0min:8sec] 
pdf/waves_gravtational/Spanish_SKA_WB_04_gws.pdf 0.53 MB saved! [ping: 396.1 ms] 

 [9/12] [0m:19 s | ETA: 0m:6 s] 
error in link https://pos.if.ufrj.br/wp-content/uploads/2021/06/Dissertacao-Joao-Cavedagne-Lobato-preliminar.pdf error: <class 'requests.exceptions.SSLError'> 

 [10/12] [0min:28sec | ETA: 0min:5sec] 
pdf/waves_gravtational/Paul-Lasky-Why-gravitational-waves-are-of-supermassive-importance.pdf 11.85 MB saved! [ping: 922.9 ms] 

 [11/12] [0min:55sec | ETA: 0min:5sec] 
pdf/waves_gravtational/ligo_CERN_040714.pdf 4.75 MB saved! [ping: 2653.9 ms] 

 [12/12] [0min:57sec | ETA: 0min:0sec] 
pdf/waves_gravtational/GRavitational_Wave_Energy.pdf 0.30 MB saved! [ping: 228.6 ms] 
```

```sh
$ ls pdf/
```

```sh
waves_gravtational/                                                                                                                              
1710.04635.pdf                     cursoGW-ICTP-Sturani1.pdf      lec005.pdf            Paul-Lasky-Why-gravitational-waves-are-of-supermassive-importance.pdf  rnoti-p684.pdf             ssi94-002.pdf
annurev.nucl.54.070103.181251.pdf  GRavitational_Wave_Energy.pdf  ligo_CERN_040714.pdf  pdf.pdf                                                                Spanish_SKA_WB_04_gws.pdf
```