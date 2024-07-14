import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Sample data, replace this with your actual data
# memory_log = {
#     "with all opt": [[0.012600245, 18748], [1.043574622, 181904], [2.880909715, 439356], [4.746978433, 450032],
#                      [6.580087388, 454812], [8.395959081, 461368], [10.229162885, 466332], [12.037321584, 470420],
#                      [13.867830914, 479540], [15.682375319, 481492], [17.114590375, 489424], [18.88665319, 487128],
#                      [20.715824796, 493432], [22.523327161, 498308], [24.340567323, 510192], [26.164078111, 509144],
#                      [27.992991493, 510196], [29.810057809, 516004], [31.624005968, 529172], [33.433013773, 531936],
#                      [35.25928479, 532344], [37.092092925, 538364], [38.102963907, 548744],
#                      [39.924327023000004, 545516], [41.729301603, 550884], [43.540291392, 557808],
#                      [45.347360579, 561724], [47.169496446, 556168], [49.011585526, 581232], [50.823214165, 574888],
#                      [52.64347461, 573316], [54.447590065, 571784], [56.276114357, 578064], [57.283435147, 570924],
#                      [59.12331606, 576356], [60.942781559, 577336], [62.764237568, 581372], [64.595277978, 575348],
#                      [66.403776621, 574876], [68.20959977, 578288], [70.019599508, 574892], [71.859492037, 567136],
#                      [73.663600443, 567480], [75.487515269, 576564], [77.133634976, 567664], [78.954270747, 578108],
#                      [80.79577953, 577728], [82.635105627, 575796], [84.447651732, 571864], [86.268515464, 578308],
#                      [88.083857798, 575500], [89.922615099, 567136], [91.729333261, 574744]],
#     "skip slice_model()": [[0.042694868, 18528], [1.054480046, 180976], [2.869932923, 303848], [4.683334884, 309164],
#                            [6.496423195, 317100], [8.303804408, 338020], [9.512667188, 339280], [11.334003168, 351248],
#                            [13.149602165, 359480], [14.967301195, 371392], [16.775008038, 375576],
#                            [18.609840614, 395792], [20.425202473, 403904], [22.232969018, 412080],
#                            [24.03805168, 416152], [25.84236809, 431664], [27.717021297, 428512], [29.498214122, 426732],
#                            [31.249602243, 438464], [33.063644976, 427312], [34.870353464, 428468],
#                            [36.673594206, 423136], [38.497763786, 429512], [40.30969706, 428276],
#                            [42.119186815, 422584], [43.96071582, 428696]],
#     "skip py_call()": [[0.037487731, 18596], [1.049279797, 183072], [2.874304285, 307504], [4.691098214, 310540],
#                        [6.506874205, 313776], [8.323560725, 317032], [10.141980121, 320264], [11.159410321, 322108],
#                        [12.975202068, 325320], [14.791966966, 328416], [16.605266190000002, 331584],
#                        [18.427664584, 334884], [20.245025925, 338292], [22.058351874, 341388], [23.890465751, 344692],
#                        [25.705545216, 347916], [27.522452603, 351332], [29.333310017, 354484], [30.352157345, 356332],
#                        [32.166749406, 360272], [33.982633515, 363588], [35.798760843, 366808], [37.614703567, 369848],
#                        [39.43130915, 373356], [41.247204044, 376604], [43.061635834, 379644], [44.878014548, 382916],
#                        [46.693206224, 385960], [48.511253715, 389324], [50.304198335, 392496], [52.118861656, 395536],
#                        [53.936806313, 398620], [55.75111513, 401740], [57.565047381, 405112], [59.38717689, 408284],
#                        [61.202498465, 411316], [63.022486377, 414684], [64.836342967, 417852], [66.646825683, 420692],
#                        [68.458628796, 423728], [70.271319163, 426908], [71.286288318, 428624], [73.101626735, 431592],
#                        [74.919554886, 434632], [76.740418829, 437672], [78.558534728, 438784], [80.373493686, 438784],
#                        [82.196832336, 438832], [84.009351503, 438832], [85.830947725, 438832], [87.646467389, 438832],
#                        [89.461031784, 438832], [90.479992122, 438832], [92.294620107, 438832], [94.111099799, 438832],
#                        [95.927230684, 438832], [97.746362444, 438832], [99.563158397, 438832], [101.383019042, 438832],
#                        [103.202695871, 438832], [105.017722804, 438832], [106.834484135, 438832],
#                        [108.647513243, 438832], [110.301242856, 438832], [112.118349192, 438832],
#                        [113.932724093, 438832], [115.74753262, 438832], [117.562538053, 438832],
#                        [119.379353309, 438832], [121.195222711, 438832], [123.010560053, 438832],
#                        [124.827020238, 438832], [126.642775797, 438832], [128.459480247, 438832],
#                        [130.281429911, 438832], [132.097044741, 438860], [133.912049601, 438864],
#                        [135.730862672, 438864], [137.54748466, 438864], [139.367069797, 438864],
#                        [141.180923526, 438864], [142.998003973, 438864], [144.813620774, 438864],
#                        [146.630798922, 438864], [148.451205105, 438864], [150.266960215, 438864],
#                        [151.284242509, 438868], [153.097853193, 438868]],
#     "del tensor input": [[0.054385368, 18624], [1.067849517, 185616], [2.901614011, 438320], [3.917688274, 436544],
#                          [5.736061766, 445896], [7.548737215, 378156], [9.366380075, 457636], [11.24744956, 463812],
#                          [13.052007021, 468808], [14.874246281, 385128], [16.732588026, 479272], [18.561360171, 485716],
#                          [20.398859579, 488532], [22.204423505, 404036], [23.793341643, 496076], [25.612309963, 446308],
#                          [27.444747921, 416448], [29.254008026, 513644], [31.088803812, 428000], [32.902038096, 521348],
#                          [34.717332123, 523908], [36.555603846, 470384], [38.365823787, 535356], [40.175110609, 538456],
#                          [42.027637158, 546492], [43.790587946, 551372], [45.556554618, 545584], [47.376132303, 559660],
#                          [49.202024759, 520548], [51.01185505, 568720], [52.823131681, 575540], [54.631675351, 566048],
#                          [56.442919021, 575484], [58.288686412, 572360], [60.100066386, 570704], [61.922948475, 567112],
#                          [63.734473112, 567968], [64.741727769, 566108], [66.578540643, 576664], [68.40184616, 574012],
#                          [70.227813142, 568888], [72.053873509, 566012], [73.872927372, 567696], [75.732145544, 565956],
#                          [77.55978126, 570304], [79.381456961, 563472], [81.195234408, 568084], [83.033166813, 563724],
#                          [84.041605986, 566292], [85.888401306, 565200], [87.735611201, 575888], [89.545348051, 572496],
#                          [91.380171848, 567764], [93.21085096, 567968], [95.031529793, 569912], [96.852397771, 564044]]
#
#     # "w/o state cache": [],
#     # "w/o memory sharing": [
#     #     [0.0144259, 20804], [1.030951876, 184876], [2.909390436, 314468], [4.738563242, 315680],
#     #     [6.553871011, 317364], [8.392857958, 319112], [9.408757094, 320844], [11.25468476, 323972],
#     #     [13.08372853, 326176], [14.921665195, 327536], [16.741873756, 329992], [18.577636054, 331960],
#     #     [20.396168183, 334424]
#     # ],
#     # "w/o all opt": [
#     #     [0.0144259, 20804], [1.030951876, 184876], [2.909390436, 314468], [4.738563242, 315680],
#     #     [6.553871011, 317364], [8.392857958, 319112], [9.408757094, 320844], [11.25468476, 323972],
#     #     [13.08372853, 326176], [14.921665195, 327536], [16.741873756, 329992], [18.577636054, 331960],
#     #     [20.396168183, 334424]
#     # ],
# }


memory_log = {
    "INDICES w/ all opt (500)":
        [[0.121695582, 18484], [1.138242638, 181748], [2.9747830459999998, 320940], [3.987460294, 321560],
         [5.800839312, 323184], [7.658348414, 326516], [9.487712467, 326400], [11.303870521, 325868],
         [13.130633692, 327504], [14.946877031, 329000], [16.767001779, 330196], [18.595238456, 336396],
         [20.426520955, 339500], [22.246760603, 340516], [23.401914615, 342672], [25.237387752, 345000],
         [27.092543988, 345908], [28.936070478, 347916], [30.769907667, 349840], [32.588460952, 351980],
         [34.407198297, 353072], [36.26201854, 352940], [38.073117, 356748], [39.899485281, 358144],
         [41.717980031, 359424], [43.410470728, 361476], [45.246525809, 363580], [47.08304573, 364392],
         [48.921582769, 366504], [50.730088897, 368588], [52.548670956, 370864], [54.38491606, 372548],
         [56.204849592, 374516], [58.036993631, 376704]],
    "INDICES w/ all opt (1000)": [[0.127972448,18972],[1.1425230339999999,182344],[3.023250693,440528],[4.869614301,442728],[5.881140066,438696],[7.722728418,461584],[9.566902625,464960],[11.418600633,467188],[13.260998155,476728],[15.075436621,482656],[16.895993632,486420],[18.713099009,491272],[20.543764888,491456],[22.356745701,495848],[24.181889821,502216],[25.194058257000002,502868],[27.065922983,512744],[28.877051902,518388],[30.694481926,520772],[32.497283935,522904],[34.324974755,532616],[36.153511945,545184],[37.966866332,546968],[39.80032964,546500],[41.625115296,531768],[43.481355493,560908],[45.154845717,566636],[46.972281601,570648]],
    # "INDICES w/o state caching":
    #     [[0.100563792, 18064], [1.118897377, 184392], [2.930504573, 240448],
    #      [4.757036424, 259204], [6.571503622, 260364], [8.391345176, 322024],
    #      [9.405164635, 261192], [11.215334633, 321952], [12.668347948, 282860],
    #      [14.481746975, 223612], [16.290405286, 229716], [18.111481906, 263500],
    #      [19.926779282, 262688], [21.737349154, 278356], [23.559145479, 202820],
    #      [25.383029608, 243320], [27.196492714, 263524], [29.006990535, 264000],
    #      [30.817628132, 264004], [32.669090061, 235100], [34.485346469, 263520],
    #      [36.344224911, 264028], [38.20003326, 324736], [40.03344474, 240224],
    #      [41.841575962, 264192], [43.650779649, 262360], [45.492965081, 323552],
    #      [47.309768098, 209584], [49.119498888, 250964], [50.934091444, 263736],
    #      [52.666107202, 264028], [54.485335287, 325004], [56.299860191, 211164],
    #      [58.124303466, 257044], [59.932058237, 264892], [61.742064053, 264044],
    #      [63.562750985, 324644], [65.389157309, 237204], [67.211464589, 264084],
    #      [69.065188937, 264556], [70.909680331, 264372], [72.668435699, 254632],
    #      [74.476232151, 264864], [76.287160483, 265056], [78.097770198, 325680],
    #      [79.921975367, 231920], [81.755673782, 266348], [83.567800662, 266140],
    #      [85.378896547, 266684], [87.198748866, 327048], [89.011459382, 238444],
    #      [90.85163399, 267076], [92.662461929, 266332], [94.475664024, 266740],
    #      [96.290895938, 206192], [98.106925493, 242560], [99.92821044, 267360],
    #      [101.739270864, 266352], [103.549015155, 314932], [105.388547294, 211140],
    #      [107.243813675, 252512], [109.066787845, 266940], [110.899699955, 265056],
    #      [112.658862415, 267492], [114.411201889, 267152], [116.230659909, 225176],
    #      [118.043691511, 266052], [119.866138065, 266532], [121.679418093, 266568],
    #      [123.49205019, 331872], [125.3188673, 239848], [127.136409308, 266860],
    #      [128.946918499, 266752], [130.765772448, 328572], [132.594755338, 211460],
    #      [133.609183432, 266900], [135.466659587, 328964], [137.283803082, 240580],
    #      [139.109874098, 266696], [140.923068614, 267176], [142.741495113, 292828],
    #      [144.553749585, 210284], [146.382762872, 253060], [148.202957519, 268796],
    #      [150.014556844, 268596], [151.839152025, 327956], [152.852950342, 268700],
    #      [154.66026038, 269164], [156.47322585, 208608], [158.29437715, 250800],
    #      [160.106453563, 268968], [161.918580082, 268912], [163.730206425, 270164],
    #      [165.546990464, 218796], [167.366960116, 258900], [169.18994029, 269140],
    #      [170.997058827, 269084], [172.667226469, 330000], [174.487908839, 210668],
    #      [176.307759449, 250476], [178.118755469, 267872], [179.930112482, 267852],
    #      [181.75050416, 328940], [183.580461694, 237104], [185.404627735, 268464],
    #      [187.245355292, 269720], [189.057196892, 269016], [190.87032826, 222208],
    #      [192.662598771, 260428], [194.486046999, 269620], [196.323757429, 269764],
    #      [198.170335456, 271112], [199.97932269, 219476], [201.811690479, 259732],
    #      [203.622604864, 270024], [205.43454496, 271264], [207.250945208, 330984],
    #      [209.096471514, 235184], [210.923005468, 270400], [212.658538406, 271488],
    #      [214.41331856, 272036], [216.23361645, 293524], [218.061712782, 216512],
    #      [219.878282706, 258460], [221.70300528, 271824], [223.527638131, 219900],
    #      [225.347331866, 259508], [227.164774619, 272136], [228.983890511, 272596],
    #      [230.797730792, 332908], [232.624081523, 239116], [233.639212992, 333100],
    #      [235.455893802, 221812], [237.282601435, 260768], [239.098350689, 272652],
    #      [240.914948838, 272340], [242.722751964, 272800], [244.540218297, 221608],
    #      [246.351139043, 263340], [248.167129247, 272260], [249.986888848, 271940],
    #      [251.81108736, 228532], [252.825941104, 272092], [254.655580551, 211264],
    #      [256.491157297, 246320], [258.315500077, 271864], [260.125336967, 271820],
    #      [261.942060782, 333540], [263.761185182, 226140], [265.581087076, 267980],
    #      [267.395748974, 272248], [269.207989771, 272136], [271.02991581, 338532],
    #      [272.65553807, 219192], [274.435703919, 260148], [276.266380358, 274084],
    #      [278.082335536, 274300], [279.902867138, 334640], [281.725641319, 237608],
    #      [283.592035339, 274248], [285.402899858, 275592], [287.214739414, 274444],
    #      [289.033156313, 214372], [290.854707008, 250508], [292.652223847, 274860],
    #      [294.470777701, 274804], [296.283670699, 276460], [298.096587697, 214716],
    #      [299.926017883, 254264], [301.751719048, 275400], [303.559750938, 275308],
    #      [305.371337853, 344108], [307.192580368, 239628], [309.017960378, 277192],
    #      [310.8295027, 284708], [312.638382628, 285996], [313.650249363, 284672],
    #      [315.461553566, 284696], [317.271444481, 285032], [319.092969939, 224828],
    #      [320.912185727, 264944], [322.723506184, 285740], [324.532111098, 285156],
    #      [326.351026282, 346340], [328.170914442, 241972], [329.994725895, 285208],
    #      [331.806220413, 285948], [332.81744029, 268856], [334.624867187, 286076],
    #      [336.438963149, 286016], [338.252383612, 346892], [340.088487548, 258372],
    #      [341.913327178, 287200], [343.721916261, 287360], [345.544905495, 261100],
    #      [347.354127822, 287732], [349.166918688, 287408], [350.979899446, 294752],
    #      [352.6588033, 228892], [354.460540947, 273716], [356.278501208, 288048],
    #      [358.117379382, 287852], [359.953256315, 230456], [361.766107619, 275936],
    #      [363.578930527, 288028], [365.393495252, 287972], [367.206908432, 349476],
    #      [369.031114874, 253072], [370.860770492, 288752], [372.650757454, 289312],
    #      [374.402024669, 288988], [376.231976612, 349868], [378.052206029, 260848],
    #      [379.882253, 290792], [381.697835914, 289424], [383.50621595, 289932],
    #      [385.330141044, 229408], [387.157681166, 269396], [388.992338651, 290200],
    #      [390.802938502, 289348], [392.61410082, 348996], [393.626398228, 288216],
    #      [395.438748561, 287856], [397.260425069, 228796], [399.086406124, 271260],
    #      [400.912888416, 289620], [402.723973977, 289192], [404.540106463, 350012],
    #      [406.350763279, 229780], [408.17086756, 266456], [409.998506827, 289772],
    #      [411.810546638, 290268], [412.821635155, 276212], [414.630136409, 290688],
    #      [416.443973835, 290136], [418.258887187, 351316], [420.086919798, 230048],
    #      [421.909975123, 270112], [423.719748241, 290904], [425.531322081, 290400],
    #      [427.367623633, 351584], [429.196155062, 230772], [431.065215182, 266444],
    #      [432.667207665, 286028], [434.486315995, 291752], [436.314416906, 242196],
    #      [438.126371731, 292320], [439.945760838, 292272], [441.757545708, 292216],
    #      [443.575093926, 233708], [445.396395413, 273620], [447.207567743, 294688],
    #      [449.02272536, 343684], [450.858328486, 236372], [452.653206084, 275556],
    #      [454.417928416, 295440], [456.228410509, 295252], [458.035847838, 306944],
    #      [459.854582282, 235812], [461.686748544, 282088], [463.494745283, 295512],
    #      [465.304985494, 295732], [467.116277922, 355176], [468.972146623, 257860],
    #      [470.797433417, 295116], [472.617529941, 294564], [473.630462709, 275244],
    #      [475.450311376, 294712], [477.264333453, 295464], [479.074463479, 294884],
    #      [480.886553029, 355788], [482.70220386, 295224], [484.514719843, 297084],
    #      [486.328442407, 337664], [487.343639575, 297216], [489.156398548, 297620],
    #      [490.970939931, 358572], [492.659563788, 238300], [494.43442067, 266980],
    #      [496.271536563, 298152], [498.094856431, 297532], [499.908074525, 342604],
    #      [501.727378077, 238692], [503.558601004, 299364], [505.371759628, 299424],
    #      [507.186615959, 360464], [509.014706224, 271188], [510.846919256, 299696],
    #      [512.659498488, 299248], [514.472160619, 346896], [516.288424421, 245304],
    #      [518.102825298, 287756], [519.915626053, 300284], [521.7271059239999, 299712],
    #      [523.561883561, 360488], [525.37432976, 267196], [527.206182976, 300140],
    #      [529.035269862, 301104], [530.846660598, 300584], [532.646186116, 361744],
    #      [534.409530526, 253080], [536.244621742, 293964], [538.055992226, 302320],
    #      [539.863344907, 301892], [541.675591485, 362432], [543.501021483, 244180],
    #      [545.321649293, 289672], [547.139600929, 302020], [549.002237515, 300520],
    #      [550.858861983, 241084], [552.66074653, 277500], [554.475323549, 300684],
    #      [556.287425472, 300204], [558.103695669, 361600], [559.928843893, 248928],
    #      [561.745625035, 290936], [563.559216405, 301240], [565.379277989, 301892],
    #      [567.192581242, 364412], [569.022666404, 274660], [570.835473214, 303980],
    #      [572.64785901, 304980], [574.463699124, 304316], [576.274410101, 243812],
    #      [578.084155947, 279384], [579.911108442, 304160], [581.723632667, 304772],
    #      [583.53846722, 365848], [585.379756896, 251480], [587.202494287, 292888],
    #      [589.027849506, 304864], [590.838204765, 304940], [592.649734409, 325416],
    #      [594.469967832, 283196], [596.299090268, 305072], [598.115049889, 305072],
    #      [599.929434742, 366412], [601.747173494, 275852], [603.563025933, 306196],
    #      [605.375964424, 307168], [607.184349689, 307848], [609.007198297, 247784],
    #      [610.826751713, 282032], [612.671370796, 307288], [614.487095599, 306768],
    #      [616.3047258, 368020], [618.11392603, 250648], [619.931932098, 292056],
    #      [621.746297764, 307480], [623.558503809, 307580], [625.374992409, 368292],
    #      [627.196822967, 269244], [629.020385991, 307740], [630.831079041, 307992],
    #      [632.650930303, 308296], [634.463723227, 254624], [636.283546652, 309228],
    #      [638.095561303, 286276], [639.915553693, 308932], [641.727546295, 307960],
    #      [643.539262859, 320344], [645.366257433, 251020], [647.191131303, 289912],
    #      [649.010110653, 307000], [650.822045983, 307672], [652.636133187, 367860],
    #      [653.78971016, 307884], [655.596547382, 307576], [657.428141851, 247276],
    #      [659.245717753, 282848], [661.06358486, 308144], [662.87549532, 308732],
    #      [664.688702103, 369244], [666.512936267, 256736], [668.327765483, 282304],
    #      [670.150683894, 311760], [671.963496328, 310976], [672.978252491, 307416],
    #      [674.795684304, 311432], [676.607863587, 312228], [678.418470062, 372304],
    #      [680.242099811, 281444], [682.064491201, 311856], [683.899819532, 311656],
    #      [685.710616225, 313060], [687.524823096, 372688], [689.355317153, 280912],
    #      [691.178108877, 312440], [692.66962048, 312836], [694.480198831, 313128],
    #      [696.294155839, 374304], [698.111337685, 264364], [699.933500958, 308984],
    #      [701.743741745, 314224], [703.559553893, 313904], [705.374458482, 253408],
    #      [707.187815229, 292212], [709.004150204, 313924], [710.819604133, 313868],
    #      [712.631374875, 314544], [713.645092916, 314972], [715.459460204, 314216],
    #      [717.27263953, 253340], [719.089026705, 290760], [720.915483293, 313948],
    #      [722.726329131, 315012], [724.585153239, 372876], [726.406728155, 263744],
    #      [728.227833694, 305460], [730.038187711, 314812], [731.854537465, 375928],
    #      [732.869395437, 315812], [734.689693502, 376872], [736.507799557, 265476],
    #      [738.329221989, 310040], [740.144179685, 316120], [741.952774426, 377104],
    #      [743.777827371, 260700]],

    "INDICES w/o memory sharing":
        [[0.128231757, 19520], [1.147440746, 181744], [2.98124313, 323320],
         [4.795169826, 325532], [6.649535844, 325872], [8.584657037, 328656],
         [10.39178697, 328680], [11.423530011, 329096], [13.231112814, 331824],
         [15.097111744, 333864], [16.954934353, 333268], [18.79797485, 334876],
         [20.656352214, 338460], [22.491083275, 341724], [24.356289473, 342804],
         [26.166081238, 344608], [27.988230744, 344672], [29.833343532, 345948],
         [31.428314612, 345188], [33.221111695, 346832], [35.092041792, 349272],
         [36.978886199, 351736], [38.844142197, 355660], [40.703248823, 357172],
         [42.541659263, 356980], [44.399230682, 360948], [46.271656595, 360460],
         [48.1403629, 360824], [49.999237771, 366148], [51.420715035, 366664],
         [53.222052214, 368132], [55.122297401, 370224], [56.995792717, 373024],
         [58.860527355, 375048], [60.709292958, 376616], [62.617643146, 377968],
         [64.489927662, 380232]]

}


# Helper function for formatting the y-axis
def mb_formatter(x, pos):
    return '{:.1f} MB'.format(x)


# Set up the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Define colors for different lines
colors = ['blue', 'green', 'red', 'purple']
# Define line styles for different lines
line_styles = ['-', '--', '-.', ':']

# Plot each configuration
for (label, data), color, line_style in zip(memory_log.items(), colors, line_styles):
    # Convert memory usage to MB
    timestamps = [x[0] for x in data]
    memory_usage = [x[1] / 1024 for x in data]  # Convert KB to MB

    ax.plot(timestamps, memory_usage, label=label, color=color, linestyle=line_style)

    # # Plot "After batch" points
    # batch_timestamps = [x[1] for x in data if x[0].startswith("After batch")]
    # batch_memory_usage = [x[2] / 1024 for x in data if x[0].startswith("After batch")]
    # ax.scatter(batch_timestamps, batch_memory_usage, color=color, s=100, edgecolors='black', zorder=5)

# Formatting the y-axis
ax.yaxis.set_major_formatter(FuncFormatter(mb_formatter))

# Adding labels and title
ax.set_xlabel('Time (s)', fontsize=14)

#plt.yscale('log')

ax.set_ylabel('Memory Usage (MB)', fontsize=14)
ax.set_title('Memory Usage Over Time', fontsize=16)
ax.grid(True, linestyle='--', linewidth=0.5)

# Show legend
ax.legend()

# Display the plot
plt.tight_layout()
# plt.show()

# Save the plot
print(f"saving to ./internal/ml/model_slicing/exp_imgs/micro_memory.pdf")
fig.savefig(f"./internal/ml/model_slicing/exp_imgs/micro_memory.pdf", bbox_inches='tight')
