saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes=0
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000
pago_con_extra=pago_mensual+pago_extra

while saldo > 0:
    # if mes<12:
    #     pago_mensual=3684.11
    #     mes+=1
    if mes>=pago_extra_mes_comienzo and mes<=pago_extra_mes_fin:
        pago_mensual=pago_con_extra
        mes+=1
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
    else:
        pago_mensual=2684.11
        mes+=1
        if saldo<pago_mensual:
            pago_mensual=saldo
            saldo=0
            total_pagado = total_pagado + pago_mensual
            print('{} {} {}'.format(mes,total_pagado,saldo))
            break
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
       
    
    print('{} {} {}'.format(mes,total_pagado,saldo))

print('Total pagado: {}'.format(round(total_pagado,1)))
print('Meses: {}'.format(mes))

# out:
# 1 2684.11 499399.2233333333
# 2 5368.22 498795.9434305556
# 3 8052.33 498190.14986151626
# 4 10736.44 497581.83215260593
# 5 13420.550000000001 496970.97978657513
# 6 16104.660000000002 496357.5822023525
# 7 18788.77 495741.6287948623
# 8 21472.88 495123.1089148409
# 9 24156.99 494502.0118686528
# 10 26841.100000000002 493878.3269181055
# 11 29525.210000000003 493252.04328026425
# 12 32209.320000000003 492623.15012726537
# 13 34893.43 491991.63658612897
# 14 37577.54 491357.4917385712
# 15 40261.65 490720.70462081523
# 16 42945.76 490081.26422340196
# 17 45629.87 489439.1594909995
# 18 48313.98 488794.37932221196
# 19 50998.090000000004 488146.9125693879
# 20 53682.200000000004 487496.748038427
# 21 56366.310000000005 486843.8744885871
# 22 59050.420000000006 486188.28063228953
# 23 61734.530000000006 485529.9551349241
# 24 64418.64000000001 484868.88661465293
# 25 67102.75 484205.063642214
# 26 69786.86 483538.4747407232
# 27 72470.97 482869.1083854762
# 28 75155.08 482196.9530037491
# 29 77839.19 481521.99697459803
# 30 80523.3 480844.22862865886
# 31 83207.41 480163.63624794496
# 32 85891.52 479480.2080656447
# 33 88575.63 478793.93226591824
# 34 91259.74 478104.7969836929
# 35 93943.85 477412.7903044583
# 36 96627.96 476717.9002640602
# 37 99312.07 476020.1148484938
# 38 101996.18000000001 475319.42199369584
# 39 104680.29000000001 474615.80958533625
# 40 107364.40000000001 473909.2654586085
# 41 110048.51000000001 473199.7773980194
# 42 112732.62000000001 472487.3331371778
# 43 115416.73000000001 471771.9203585827
# 44 118100.84000000001 471053.5266934101
# 45 120784.95000000001 470332.13972129935
# 46 123469.06000000001 469607.7469701381
# 47 126153.17000000001 468880.33591584704
# 48 128837.28000000001 468149.8939821631
# 49 131521.39 467416.40854042216
# 50 134205.5 466679.8669093406
# 51 136889.61 465940.2563547962
# 52 139573.71999999997 465197.56408960785
# 53 142257.82999999996 464451.77727331454
# 54 144941.93999999994 463702.8830119534
# 55 147626.04999999993 462950.8683578365
# 56 150310.15999999992 462195.7203093275
# 57 152994.2699999999 461437.42581061635
# 58 155678.3799999999 460675.9717514939
# 59 158362.48999999987 459911.34496712516
# 60 161046.59999999986 459143.5322378215
# 61 163730.70999999985 458372.5202888124
# 62 167414.81999999983 456598.2957900158
# 63 171098.92999999982 454816.6786891408
# 64 174783.0399999998 453027.6381836789
# 65 178467.1499999998 451231.14334277756
# 66 182151.25999999978 449427.1631067058
# 67 185835.36999999976 447615.6662863171
# 68 189519.47999999975 445796.6215625101
# 69 193203.58999999973 443969.9974856872
# 70 196887.69999999972 442135.7624752109
# 71 200571.8099999997 440293.8848188576
# 72 204255.9199999997 438444.3326722695
# 73 207940.02999999968 436587.07405840396
# 74 211624.13999999966 434722.07686698064
# 75 215308.24999999965 432849.3088539264
# 76 218992.35999999964 430968.7376408178
# 77 222676.46999999962 429080.33071432123
# 78 226360.5799999996 427184.0554256309
# 79 230044.6899999996 425279.87898990436
# 80 233728.79999999958 423367.76848569565
# 81 237412.90999999957 421447.6908543861
# 82 241097.01999999955 419519.6128996127
# 83 244781.12999999954 417583.50128669443
# 84 248465.23999999953 415639.3225420557
# 85 252149.3499999995 413687.0430526476
# 86 255833.4599999995 411726.629065367
# 87 259517.56999999948 409758.04668647266
# 88 263201.67999999947 407781.26188099966
# 89 266885.78999999946 405796.2404721705
# 90 270569.89999999944 403802.9481408046
# 91 274254.0099999994 401801.35042472463
# 92 277938.1199999994 399791.412718161
# 93 281622.2299999994 397773.1002711534
# 94 285306.3399999994 395746.37818894984
# 95 288990.4499999994 393711.2114314038
# 96 292674.55999999936 391667.564812368
# 97 296358.66999999934 389615.40299908625
# 98 300042.77999999933 387554.6905115824
# 99 303726.8899999993 385485.39172204735
# 100 307410.9999999993 383407.47085422254
# 101 311095.1099999993 381320.8919827818
# 102 314779.2199999993 379225.6190327101
# 103 318463.32999999926 377121.6157786797
# 104 322147.43999999925 375008.8458444242
# 105 325831.54999999923 372887.2727021093
# 106 329515.6599999992 370756.85967170144
# 107 333199.7699999992 368617.56992033357
# 108 336883.8799999992 366469.3664616683
# 109 340567.9899999992 364312.2121552586
# 110 343252.09999999916 363146.0697059055
# 111 345936.20999999915 361975.0683296801
# 112 348620.31999999913 360799.1877810538
# 113 351304.4299999991 359618.40773014154
# 114 353988.5399999991 358432.70776235044
# 115 356672.6499999991 357242.0673780269
# 116 359356.7599999991 356046.465992102
# 117 362040.86999999906 354845.88293373573
# 118 364724.97999999905 353640.29744595964
# 119 367409.08999999904 352429.6886853178
# 120 370093.199999999 351214.03572150663
# 121 372777.309999999 349993.3175370129
# 122 375461.419999999 348767.5130267505
# 123 378145.529999999 347536.6009976953
# 124 380829.63999999897 346300.56016851903
# 125 383513.74999999895 345059.3691692212
# 126 386197.85999999894 343813.00654075964
# 127 388881.9699999989 342561.45073467947
# 128 391566.0799999989 341304.68011274067
# 129 394250.1899999989 340042.6729465438
# 130 396934.2999999989 338775.4074171544
# 131 399618.40999999887 337502.8616147259
# 132 402302.51999999885 336225.0135381206
# 133 404986.62999999884 334941.84109452943
# 134 407670.7399999988 333653.32209909
# 135 410354.8499999988 332359.43427450286
# 136 413038.9599999988 331060.15525064664
# 137 415723.0699999988 329755.462564191
# 138 418407.17999999877 328445.3336582085
# 139 421091.28999999876 327129.74588178436
# 140 423775.39999999874 325808.6764896251
# 141 426459.5099999987 324482.10264166526
# 142 429143.6199999987 323150.0014026722
# 143 431827.7299999987 321812.34974185
# 144 434511.8399999987 320469.124532441
# 145 437195.9499999987 319120.3025513262
# 146 439880.05999999866 317765.8604786234
# 147 442564.16999999864 316405.77489728434
# 148 445248.27999999863 315040.0222926897
# 149 447932.3899999986 313668.57905224257
# 150 450616.4999999986 312291.42146496027
# 151 453300.6099999986 310908.5257210643
# 152 455984.7199999986 309519.8679115687
# 153 458668.82999999856 308125.4240278669
# 154 461352.93999999855 306725.1699613164
# 155 464037.04999999853 305319.0815028219
# 156 466721.1599999985 303907.134342417
# 157 469405.2699999985 302489.3040688438
# 158 472089.3799999985 301065.5661691306
# 159 474773.4899999985 299635.8960281687
# 160 477457.59999999846 298200.26892828604
# 161 480141.70999999845 296758.66004882054
# 162 482825.81999999844 295311.0444656906
# 163 485509.9299999984 293857.39715096436
# 164 488194.0399999984 292397.6929724267
# 165 490878.1499999984 290931.90669314517
# 166 493562.2599999984 289460.0129710333
# 167 496246.36999999837 287981.9863584126
# 168 498930.47999999835 286497.80130157265
# 169 501614.58999999834 285007.4321403292
# 170 504298.6999999983 283510.85310758057
# 171 506982.8099999983 282008.03832886217
# 172 509666.9199999983 280498.9618218991
# 173 512351.0299999983 278983.59749615705
# 174 515035.13999999827 277461.919152391
# 175 517719.24999999825 275933.9004821927
# 176 520403.35999999824 274399.51506753516
# 177 523087.4699999982 272858.73638031655
# 178 525771.5799999982 271311.5377819012
# 179 528455.6899999982 269757.8925226591
# 180 531139.7999999982 268197.77374150354
# 181 533823.9099999982 266631.15446542646
# 182 536508.0199999982 265058.0076090324
# 183 539192.1299999981 263478.30597407004
# 184 541876.2399999981 261892.02224896202
# 185 544560.3499999981 260299.12900833273
# 186 547244.4599999981 258699.59871253412
# 187 549928.5699999981 257093.4037071697
# 188 552612.6799999981 255480.51622261625
# 189 555296.789999998 253860.90837354382
# 190 557980.899999998 252234.5521584336
# 191 560665.009999998 250601.41945909374
# 192 563349.119999998 248961.48204017332
# 193 566033.229999998 247314.71154867404
# 194 568717.339999998 245661.0795134602
# 195 571401.449999998 244000.55734476628
# 196 574085.559999998 242333.1163337028
# 197 576769.669999998 240658.72765175992
# 198 579453.7799999979 238977.36235030895
# 199 582137.8899999979 237288.9913601019
# 200 584821.9999999979 235593.585490769
# 201 587506.1099999979 233891.1154303139
# 202 590190.2199999979 232181.55174460687
# 203 592874.3299999979 230464.86487687606
# 204 595558.4399999978 228741.0251471964
# 205 598242.5499999978 227010.0027519764
# 206 600926.6599999978 225271.76776344297
# 207 603610.7699999978 223526.29012912398
# 208 606294.8799999978 221773.53967132868
# 209 608978.9899999978 220013.4860866259
# 210 611663.0999999978 218246.09894532018
# 211 614347.2099999978 216471.3476909257
# 212 617031.3199999977 214689.2016396379
# 213 619715.4299999977 212899.62997980308
# 214 622399.5399999977 211102.6017713856
# 215 625083.6499999977 209298.08594543306
# 216 627767.7599999977 207486.05130353905
# 217 630451.8699999977 205666.4665173038
# 218 633135.9799999977 203839.30012779258
# 219 635820.0899999976 202004.5205449917
# 220 638504.1999999976 200162.09604726252
# 221 641188.3099999976 198311.9947807928
# 222 643872.4199999976 196454.1847590461
# 223 646556.5299999976 194588.6338622088
# 224 649240.6399999976 192715.3098366347
# 225 651924.7499999976 190834.18029428736
# 226 654608.8599999975 188945.21271218025
# 227 657292.9699999975 187048.37443181433
# 228 659977.0799999975 185143.63265861355
# 229 662661.1899999975 183230.9544613578
# 230 665345.2999999975 181310.30677161345
# 231 668029.4099999975 179381.65638316184
# 232 670713.5199999975 177444.96995142504
# 233 673397.6299999974 175500.21399288933
# 234 676081.7399999974 173547.35488452637
# 235 678765.8499999974 171586.3588632119
# 236 681449.9599999974 169617.19202514197
# 237 684134.0699999974 167639.82032524672
# 238 686818.1799999974 165654.20957660192
# 239 689502.2899999974 163660.32544983778
# 240 692186.3999999973 161658.13347254545
# 241 694870.5099999973 159647.59902868106
# 242 697554.6199999973 157628.68735796722
# 243 700238.7299999973 155601.3635552921
# 244 702922.8399999973 153565.59257010583
# 245 705606.9499999973 151521.3392058146
# 246 708291.0599999973 149468.56811917218
# 247 710975.1699999972 147407.24381966874
# 248 713659.2799999972 145337.33066891736
# 249 716343.3899999972 143258.79288003786
# 250 719027.4999999972 141171.59451703803
# 251 721711.6099999972 139075.69949419238
# 252 724395.7199999972 136971.0715754182
# 253 727079.8299999972 134857.67437364912
# 254 729763.9399999972 132735.471350206
# 255 732448.0499999971 130604.4258141652
# 256 735132.1599999971 128464.5009217242
# 257 737816.2699999971 126315.65967556472
# 258 740500.3799999971 124157.8649242129
# 259 743184.4899999971 121991.07936139712
# 260 745868.5999999971 119815.26552540294
# 261 748552.709999997 117630.38579842544
# 262 751236.819999997 115436.40240591888
# 263 753920.929999997 113233.27741594354
# 264 756605.039999997 111020.97273850997
# 265 759289.149999997 108799.45012492042
# 266 761973.259999997 106568.67116710759
# 267 764657.369999997 104328.59729697053
# 268 767341.479999997 102079.1897857079
# 269 770025.5899999969 99820.40974314835
# 270 772709.6999999969 97552.21811707814
# 271 775393.8099999969 95274.57569256597
# 272 778077.9199999969 92987.443091285
# 273 780762.0299999969 90690.78077083202
# 274 783446.1399999969 88384.54902404382
# 275 786130.2499999969 86068.70797831067
# 276 788814.3599999968 83743.21759488697
# 277 791498.4699999968 81408.037668199
# 278 794182.5799999968 79063.12782514983
# 279 796866.6899999968 76708.44752442128
# 280 799550.7999999968 74343.95605577303
# 281 802234.9099999968 71969.61253933875
# 282 804919.0199999968 69585.37592491932
# 283 807603.1299999967 67191.20499127316
# 284 810287.2399999967 64787.058345403464
# 285 812971.3499999967 62372.89442184264
# 286 815655.4599999967 59948.67148193365
# 287 818339.5699999967 57514.34761310837
# 288 821023.6799999967 55069.88072816299
# 289 823707.7899999967 52615.228564530335
# 290 826391.8999999966 50150.34868354921
# 291 829076.0099999966 47675.19846973066
# 292 831760.1199999966 45189.7351300212
# 293 834444.2299999966 42693.915693062954
# 294 837128.3399999966 40187.69700845071
# 295 839812.4499999966 37671.03574598592
# 296 842496.5599999966 35143.888394927526
# 297 845180.6699999965 32606.211263239726
# 298 847864.7799999965 30057.960476836557
# 299 850548.8899999965 27499.091978823373
# 300 853232.9999999965 24929.561528735136
# 301 855917.1099999965 22349.32470177153
# 302 858601.2199999965 19758.33688802891
# 303 861285.3299999965 17156.55329172903
# 304 863969.4399999965 14543.928930444567
# 305 866653.5499999964 11920.418634321419
# 306 869337.6599999964 9285.977045297757
# 307 872021.7699999964 6640.558616319831
# 308 874705.8799999964 3984.117610554497
# 309 877389.9899999964 1316.6081005984738
# 310 878706.5981005948 0
# Total pagado: 878706.6
# Meses: 310