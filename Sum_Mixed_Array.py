'''Sum Mixed Array
8 kyu
Python

DESCRIPTION:
Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.

TAGs:
  FUNDAMENTALS
  STRINGS
  ARRAYS
'''

# Solution 1
def sum_mix(arr):
    return sum([a if type(a) == int else int(a) for a in arr])


# Solution 2
def sum_mix(arr):
    return sum(map(int, arr))


# Solution 3
def sum_mix(arr):
    return sum(int(n) for n in arr)

  
# Solution 4
def sum_mix(arr):
    result = 0
    for a in arr:
        try:
            result += a
        except TypeError:
            result += int(a)
    return result

  
# Solution 5
def sum_mix(arr):
    somme = 0
    for i in arr:
        somme += int(i)
    return somme;

  
# Solution 6
def sum_mix(arr):
    return sum(int(x) for x in arr)

  
# Solution 7
from functools import reduce

def to_int(num):
    "convert to int digit or string"
    try:
        return int(num)
    except ValueError:
        return 0

def sum_mix(arr):
    """
    Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
    Return your answer as a number.

    :param arr: [9, 3, '7', '3']
    :return: 22
    """
    converted_array = list(map(lambda x: to_int(x), arr))
    return reduce(lambda res, x: res + x, converted_array)


# Solution 8
def sum_mix(arr):
  L = []
  for i in arr:
    L.append(int(i))
  return sum(L)


# Solution 9
sum_mix = lambda a: sum(map(int, a))


# Solution 10
sum_mix = lambda A: sum( [int(n) for n in A] )


# Bonus Solution ;^)
sum_mix = lambda x : sum([int(SoasajokeIwenttomyfriendshousewearingPekoraswigandclothesIcouldbarelystopmylaughterashewentasredasatomatoandlookedatmefromheadtotoewithabitofdroolinhismouthThewayhestaredmademdefeelabitfunnytoobutIdecidedtoteasehimmorebytakingoffmyclothesHeaskedmeAreyouseriousandIsaidYeppekoHewentsilentforwhatseemedlikeforeversoIaskedhimWhatsthematterpekoHesaidhesconfusedbutthenhisbonergotreallyhardwhichmademetakeoffhisclothesIexpectedhimtoscreamStopasIkissedhimandstrokedhiscockbutheinsteadshoutedOhGodPekorawhichmademegetabonermyselfBeforeIknewitIwasblowinghimforthefirsttimetillhecameHissemenwassothickitgotstuckinsidemythroatnomatterhowhardIswallowedHethensaidIwanttofuckyounowandseeingthatwevealreadygonethatfarandwewerebothnakedIobligedAfewhourslaterthejerkwentallpaleandsaidtomeWhydidwedothatNowImnotfuckingstraightButhestilllookedsocuteallconfusedlikethatsoItookpityonhimandreassuredwhilewipinghiscumoffmyfaceLetsjustpretendImstillPekora) for SoasajokeIwenttomyfriendshousewearingPekoraswigandclothesIcouldbarelystopmylaughterashewentasredasatomatoandlookedatmefromheadtotoewithabitofdroolinhismouthThewayhestaredmademdefeelabitfunnytoobutIdecidedtoteasehimmorebytakingoffmyclothesHeaskedmeAreyouseriousandIsaidYeppekoHewentsilentforwhatseemedlikeforeversoIaskedhimWhatsthematterpekoHesaidhesconfusedbutthenhisbonergotreallyhardwhichmademetakeoffhisclothesIexpectedhimtoscreamStopasIkissedhimandstrokedhiscockbutheinsteadshoutedOhGodPekorawhichmademegetabonermyselfBeforeIknewitIwasblowinghimforthefirsttimetillhecameHissemenwassothickitgotstuckinsidemythroatnomatterhowhardIswallowedHethensaidIwanttofuckyounowandseeingthatwevealreadygonethatfarandwewerebothnakedIobligedAfewhourslaterthejerkwentallpaleandsaidtomeWhydidwedothatNowImnotfuckingstraightButhestilllookedsocuteallconfusedlikethatsoItookpityonhimandreassuredwhilewipinghiscumoffmyfaceLetsjustpretendImstillPekora in x])
""" let's pretend i'm still pekora
                                     +*..................................................................................;.................`     `````
                                    .x...........................................................................,,......:;................`  ````````
                                    #*............................................................................:,......i,..............`   ````  ` 
                                   .x,...........................i.................................................;......,:.............`           :
                                   iz...........................,;......................................................................`          `*+
                                  `n;...........................;,...................................................;......,..........``         :#;.
                                  ,x............................;,..................,,...............................i,.....:*.........``       .++...
                                  +#............................i....................i...........................` `..*......+..........`     `iz:....
                                 `xi............................*....................i...........................`  ..:;.....,+........`    `iz;......
                                 .M,............................+....................;,...........................  ...+......+,.......`  .*z:........
                                 ;n.............................#....................,+.....................``.....`...,i.....,*......`.i+*,,;........
                                 *#............:................#.....................z...................`.` `.........*,.....+,....:;;:....i;.......
                                `z*............;................#.....................*;..`...............``.`..........,*.....,*.............*:......
                                .x,............i...............,#.....................,#................`................*:.....#.............,+,.....
                                :x.............*...............,#......................n:..`````````....```.....`````````,*.....;i.............,#.....
                                *z.............*...............;+......................+#..`````````...`````....````````.`i:.....#..............:#,...
                              `iM+.............*...............*+.....................`,x:.```....```..`````````````....`.,+.....*;..............,##+#
                              +xni.............i...............z#..........`........````nn..``````````..``````````````....`i;.....+................;zz
                             *x:*;............................:M#.........``....``..````*Mi..```````.`...``````````````````.#...`.+:..............:;+#
                            ,M;.+:............................iM#.......``````````..````.nx,```````````.,.``````````````````;*..`.:*..............;;*z
                           `x+..#..............*..............#zn`......``````....```````*n#.```````````.,.````````````````..+,...`+.............:;;*z
                           *x,..#..............+............`.nin...`````````````````````.##*,;:::;.`````.,.```````````````..,#...`ii...........,;;;*z
                          `M;..,#..............+........``...;z;#.``````..````````````````i+n#.```.:.`````,;,.```````````.````;*.``,+`..........;;;;*n
                          *x...,#..............+........``...+*;+,````````````````````````.z*++.````:``````i;:,.``````````````.*;`.`*:.........:;;;;*z
                         `xi...:+..............:.....```....`#;;+;````````````````````````:i+i+#:```:```````*i::,.```````````.`.+:..:+........:;;;;;*z
                         :x....:+....................```....,#;;i+```````````````````````,,`+iiiz*,`:````````*+;::,.````````````.#:..#`......:;;;;;;+#
                         zz....;*..............,..``...`````i+;;;z```````````````````````;``,+.:;*n+i.````````iz+;::,.``````````..+:`i;.....:;;;;;;;#+
                        .M;....:+..............+```````.````#i;;;#.``````````````````````:```ii..:;z#z+;,.`````,#nz+i;:,...``````..*;,#...,;;;;;;;;;z*
                        :x.....;#..............+....``..```.#;;:;**``````````````````````,````+,..i;.:;*#zzz#+**+z#iz#znnzz##*i;;:::i;#..:;;;;;;;;;;ni
                        *z.....:z..............+....``..```,#;:.;;n.`````````````````````,````.z.,+`````...,:::;;;;**;;;i*;;;;:,..,,..ii;;;;;;;;;;;;x:
                        ##.....,#............`.#..`````.```**;,`.;++:,,,::.``````````````,`````,z*`````..````````.;M::,,,+;:.````````.,z;;;;;;;;;;;;M.
                        n*.....,#............`.#``````..```z;;.``;zn.````.,:`````````````:````.;i*```:*;.````:+nMWWWWWWMxn+:.``.,````..#;;;;;;;;;;;*x`
                       `x;......#`..........``.#``````..`.`z;:``.#:*#``````.:````````````.::::,``i;,i:````izMWWWWWWWWWWWWWn+;,:,.``````i*;;;;;;;;;;## 
                       `x;.....`#...........``.#.`````..`.,+;,``:;.:#i``````:#`````````````..`````**.``.*xWWxWWWWWWWWWWWWWM#*i.```````.,z;;;;;;;;;;n; 
                       `xi.....`#,...``.``.````#..````..``**;.``:;..:zi``````z#,`````````````````.:*.`:nWWWMnWWWWx+;**##nMWz+i`````````.n;;;;;;;;;;M. 
                       `xi......+;...` ` `..```+,`````..``#i:````+...:zi`````,n#i.`````````````.i**..+WWMMWWMMMxMMWz;::::;+n+i,`````````*i;;;;;;;;*x  
                       `n+......*i.... ```.`.`.i:.````..``n;,````.#,..,+#.````#*izzi:,....,:i++*:,,:xWWMMMWMxxxnnnnMW+:::::+ii;````````.:#;;;;;;;;z+  
                       :M#......i+....``.....`.:i.````..`.#;```````;#;..;z;`,;.+:.:;*#zzzz#i:.`.,,iWWWWWWMxMn*:;+xnnnW#::::*+.;````````..z;;;;;;;;M,  
                      ;MMn......:z.......`````.,+`````..`;*:`````````,i*++#ni``.+,`````````````,,:MWWWWWMxx:     .xnnnMi```,z..``````````:;;;;;;;*x`  
                     ;M+:x.......z........````..#.````..`+i.```````````````.;++;.+:````````````,,+WWWnzMx#`       ;xnnnM,  `+,```````````,;;;;;;;z#   
                    in:``z:......#:.....``.`````#.````..`z;```````````````````.:;:*;```````````.:iWWz:nxn`        ,xznnx# ` ;i``````````..*;;;;;;x,   
                   in,   ,#......*+.....``.`````+,````...n:```````````,;;;;;;,`````,.```````````.*Wn:;xx;         #nzzzzM,  ,#``````````.`n;;;;;*x`   
                  ;n,     +,.....i#.......``````i;````..,z,`````````;;;:...,:i,.`````````````````+x;:iMx`         *nzzzzx*` .n````````````#i;;;;z+    
                 ,x,      ,*.....**,......``````,+````..;+.````````.`````.,,,,,,.````````````````*:,:ixn`     `   +zzz##zz `.#.```````````i*;;;ix.    
                `x;       `z.....*ii......```````#.```,.i*```````````.,:i**+*i:,,.```````````````.`,,ixn;   .in`.*n######n``.i:``.```````.,#;;;#z     
                *z         *:....i:#......```````#:```,,+;````````,ixWWWWWWWWWz*:,```````````````````*nznii+xznnnz*;:::+#x...:+``.```````..z;;ix:     
               `x,         .+...,::#.....,`.`````;i```,,#:``````,zWWWWxMWWWWWWWn:.```````````````````*nzzzz#######:::::;#x,...z``.```````.`zi;nz      
               ,n`          z...;:,i*...`,.```````+.``,,z:.```:nWWnxWWMMWWWWMMWWx,```````````````````;nzz###i+####::::::#x,...n``.```````..+nnM,      
               iz        `  +:..*+#*z..``,,``.````+:``,:z.;+i#WWWWMnWWMMMxxxM#;;*+```````````````````,nz##;:::+##i::::::#n:,..z.`.```````..;xM*       
               *+        `  ;z#z*:,.*:.`..,...````:*``.:z``,MWWWWWWMxxx#*+xxnxn:.`````````````````````###i::::::,....,:in*,,..+,`.```````.`,x#`       
               *+        `` ,+i*.....z....,,`.`````+,`.;#`,xWWWWxWxxni`   .#xnnn,```````...```````````;n#i::::,.......,#x,,:..i:`..`````....x:        
               i#        `` ,+#,.....*:...,:,.`````:i`.;#.xWWWx*xMxz.      .xnzx#``````....````````````+z+::::.......i+#i,.:..:;`..`````....z;        
               :n`       `` ,z;.......#.``.,:```````*,.;+zWWWMi*Wxx.        nzzzMi`````....````````````.#ni:::....;,,*;.,:.,:`:*`..`````.`..+*        
               .M.       ```,+........*i...,:,`.````:*.;#WWWMi:#Mxi        `xzzzzn`````....``````````````iz+;,.,.++:,.:,.:..:`,+...`````.`..*#        
                zi       `.`,i.........z,..,i:...````*:iMWWW*::nxx`        +zz###x;`````.````````:.```````.*z+++.,:,:.,:.,,.,.,#....``..`.,.;n`       
                :x`      `.`.;.........z#.`,;;:`.````:*iWWWz:::xxx`        ;zz####+``````````````,,``````````.....:.:..:..:```.z.,..``..`.,.,x.       
                .x*      `.`.,........:#ni..:+:,.````.##WWWi::,znx;``.;z` ,n#+ii+#z``````````````i`````````````...,,,,..:.,,``.z...`````..,..n:       
               .x;z,     `...,........n::x,.,+i:,```,:izWWn:::`#nnnnnnzn+zn#;::::#z,```````````.i.```````````````..:.:..,,````.z.,.`````..,..#i       
              `n;.,z`    `..;:,......iz` *n..:xi:,````.nxW*::.`ixzzz########;::::*z:``.,```:::i+```````````````````.,.,```````.z.,.````...,..+*       
              ;#...;+`   `..i,......,x.  `##.,#M+,,.```i+W*:,``,Mzz###++####:::::*n,``:```,+i;;*```````````,`.``````,..```````,z,,.````...,..*+       
             `......**   `..;,..`..,n;    .z*.:xx#:,..`.z+*:`  `zz##+i::i++i:::::*#```.;:;+i:;;*```````````.,.```````````````,;z,,.```....:..*#       
             `.......+i  `........,n*      .ni.+xi#*:,.`ii:,`   :M##;::::::,,,,::#*````.,,ii;;i;````````````````````````````,in#,,.```....:,.iz       
            :#........#: `.......:n*        ,xi,n;:+#*:..z,,.`  `#z#;::::,.....,;n,````````:ii;``````````````````.`,``````.,*MW+,..`......:..iz       
            i#........:z,``.....izz          ,xii+,,;+#*:;i,,.```.x#*:::,......:#i```````````````````````````````.,,`````,:#Wxn+,.........:..iz       
            i#.....,...i#``...:+i.n`          ,x*#i..:;i#*z,,,.`` ,x#i::,...,.*+,``````````````````````````````````````.,;nWxxMi,........,:..iz       
            ;z.....,...:*i`.,*+. `n,           `n+z:..,:;;z;,,,,.``:xz*:,.i#+,...`````````````````````````````````````,:*#+;::#:.........::..*#       
            ,x.....,,...;*:#+*;..,zxnnnxxxxxnn#i;nzz,....,;#,,,,,,..,#xxni:.,:..````````````````````````````````````.:izz;,:::z,.........::..++       
            `zi....,:,;*zxMMxxn#*i:,,,::::::;;i#MWxnz,...`.z;.,,,,:,:,,;,.:..:..``````````````````````````````````.:;*#i::::::z,.........:;..#i       
          ``,zzi#nxxn+*;,.``                    `#i*Mn,.`..,z,...,:,,:,:,,,:..:.````````````````````````````````.,;+zi:::::::;+..........:*..x:       
     `,*#nMWMz+i:,.`                             `#:,+n,....#i...,,:,::,:..:,.,,``````````````````````````````.,:in*:::::::::+,.........:i*.;x`       
`:*#xxn#*;,.`                                     .#,.;n:....z;....:,.:,::..:...````````````````````````````.,::i#;,,.``   `,z..........:n;.#+        
Mxz*:`                                             ;+..:x,...,n;....:.,:.:,..,```````````````````````````.,::;;i#:.`        i;..........+M,,x,        
,`               .:;iii;.                           +i..:x....,n*...:,.:,.:.``````````````````````````.,;;;;;;;#:          .#..........i#z.z+         
               ,*+,`` `.*+`                         .z...iz.....#n:..:,.,.````````````````````````..:;;;;;;;;;#;          `+,.........;#*:+n`         
             `*;`        .z`                         ;+...zi.....iMn:..````````````````````````.,;;;;;;;;;;;iz*`          *i.........*#:#+M.          
             *,           ;,                         `z,..,x,....:+xWM#:.``````````````````,;*#zzzzz*;;;;;;+#.           ii........:zi:z++x`          
            :;            ;:                          :z...iz....,ix.;#MWxz#*:,,,,,,:i+++*#+i;:::,::#+;;;;+i            ii.......;#+:::::znn`         
            i`           `#.                           #:...zi....:z;  `,;*#nWWWWWWWWx;;:::::::::::,:i*+#z#            i:.....:+#*;:::::i+;nz`        
            i`          `+:                            .n...,n,....ix`       ``````.z:`:::::::::,,::::::*+,          ,**i*;;i**;:::::::;z;;.n+        
            ;;        `i+:`                             +i...++....:zi             i* ,:,,,,::::,,::::;#;`           ,::,.``````.::::,i#i;.`,xi       
            `ii,...,;*+;`                               .n...,n,....;x.           .n.`::::,,::::::::::,.                         .::::z;;:```;M:      
              .i++**;.                                   **...iz..,..##`          ;# .::::,,:::::::::*`                           ,::*#;:`````*x`     
                                                         `x,...z:..,.,n*          *i ,::::,,::::::,,+;                            .::z;;.``````z#     
                                                          **...;z...,,:x;         +i`:::::,,::::::,,#`                            .,:;:.```````,M:    
                                                          `x,...z:...:,ix;       ;z`,:::::,::::::::*;                           `:i:;:``````````*x`   
                                                           i+...:n....,:ix;      #;`::::::,::::::::#```.*:`                    `;z*;,```````````.Mi   
                                                            n:...z:.....:ix+`   `n.,:::::,,,,,:::::i ``:`,;                   `:ni;.`````````````;M`  
                                                            i#...:n......,;zx*` .z`,:::::,,,,,::::;;  :#`i`                  `izi:.```````````````Mi  
                                                            `z:...z:...`...,izxz+n.,::::,,,,:,,:++*:    ;i``            `...:##;.```````````i*,``.WM` 
                                                             i#...:n..........*xxx:,::::,,,,::i+:`      ````           .i*+zxMz:```````````*i;++;inW, 
                                                           ` `n:...n:......:i+zi.i+`:::::::::;#``.` `                 .*xMMMMMWW*.````````*;,,,:*z+x+ 
                                                          `.` ;z...;z:;i*#xn+:`  .z`:::::::::*:.::.`*`              `.*xMMMMMMMWWni;;:,``;i,,,,,:#nnM;
                                                         `..` `n,...nMnz#i.      `z;,:::::::;#,.:,`#;`.``,    `:i;;*+nMMMMMMn+izWWMnznxx++,,,,,,i;.nxn
                                                        `....` ;z...;W.           ,n#ii+#####+#.`,#n.,:..x*:,;z#i+#MMMMMMxz;`  `zMM#+*+n#+i:,,,:#` `;.
                                                       `.....` `x,...xi            .W**;;;;;#xMxxz;#`::.:#i*+i::;+WMMMMx+.  ``` .nMz+#x; `:+#+;+:     
                                                      `.......` i#...*x`           ,W;;;;;*+MWWWWWx+ :, *;:,.```+WMMMx*.  `.....`iMznz.     `.:,      
                                                     `........` `x,,,.M;           *Mz;;;;+,:+xMWWWx.` :#``````#WMMMz,  `..`   ..,xx;`                
                                                   `...........` *+::.#n           znnz;;+i`` `:+xMMz:ix*`````zMMMxi` `..`      .i+`                  
                                                 ``............``.M:,,:M,         `x#zxznx,`...``.;#xMMWWxi``#MMMz, `..`        `#`                   
                                               ``...............` #i::,z+         .W+nxx*n.   `...``,*nMWWWnzWMM*` ..`          *:                    
"""
