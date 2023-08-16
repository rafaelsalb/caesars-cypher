import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from caesar import encrypt_msg, decrypt_msg_brute


def test_encrypting1():
    msg = "If he had anything confidential to say, he wrote it in cipher, that is, by so changing the order of the letters of the alphabet, that not a word could be made out."
    new_msg = encrypt_msg(msg, 7)
    proof = "Pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba."
    assert proof == new_msg


def test_encrypting_lorem_ipsum():
    msg = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris sed ante malesuada odio venenatis ultricies sed sit amet nibh. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam eget augue elit. Sed imperdiet ante felis. Nulla iaculis sem blandit libero egestas, ut cursus leo lacinia. Suspendisse vitae ex iaculis, ornare leo quis, posuere quam. Phasellus et elementum libero, mattis accumsan turpis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Praesent enim mauris, finibus sed tincidunt sit amet, egestas at metus. Aenean sed pulvinar nunc. Duis egestas mauris in eros dignissim, lobortis fringilla erat maximus.

    Sed in efficitur lorem. Vestibulum pellentesque pretium sodales. Nunc ut nibh at lorem varius porttitor. Nullam sem orci, maximus sit amet euismod at, aliquet faucibus nibh. Phasellus ut eros vitae mauris faucibus sodales accumsan eu odio. Sed turpis tortor, laoreet nec sapien at, maximus posuere magna. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Nullam finibus elementum metus non imperdiet. Donec aliquam nisi vitae luctus mattis. Phasellus faucibus magna eget diam tristique fringilla. Cras maximus, velit at hendrerit dapibus, mi nulla convallis mi, quis tristique libero nulla sed dolor. Pellentesque pharetra finibus enim, non pharetra leo viverra vel. Proin dolor justo, interdum eget orci id, dapibus viverra nunc. Proin tincidunt mi non lacus ornare, ac pharetra nulla accumsan. Nullam malesuada rutrum magna eu tincidunt. Sed sed tempor tellus.

    Aenean porta metus sit amet mauris tristique malesuada. Phasellus feugiat, erat vitae eleifend dapibus, nulla eros efficitur dolor, a hendrerit ex massa quis velit. Phasellus enim velit, egestas quis ex eu, pellentesque sollicitudin tortor. Nullam placerat, augue quis elementum aliquet, magna tellus vehicula urna, ut sagittis sem sem sed enim. Nunc eget leo ac eros pulvinar tempor lacinia blandit dolor. Morbi accumsan maximus volutpat. Maecenas efficitur faucibus metus non consectetur. Maecenas nunc ante, semper et sapien ac, pharetra faucibus nisi. In blandit libero bibendum metus fermentum sollicitudin. Duis auctor sed dolor et viverra. Ut rhoncus dolor non arcu porttitor, vel tristique sapien fringilla. Donec eget sem felis. Donec aliquet laoreet tincidunt.

    In hac habitasse platea dictumst. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Etiam efficitur lobortis justo, viverra tempor risus sagittis ullamcorper. Mauris ut augue magna. Donec aliquam justo at lacus feugiat, vel ultrices massa elementum. Etiam ac consectetur diam. Maecenas ut est viverra, cursus odio non, dapibus ante. Nunc non ante dui. Cras id tincidunt justo, nec ultricies neque. Donec sed dui at ipsum viverra facilisis non ullamcorper tortor. Sed porttitor consequat nisi, vel facilisis purus interdum sed. Donec sit amet nisi augue. Suspendisse sit amet volutpat elit, eget porttitor risus.

    Donec eu sapien id leo tempor viverra. Nunc ut imperdiet lorem, ac pellentesque quam. In varius mi volutpat, hendrerit est a, elementum ligula. Mauris sit amet lobortis arcu, ac condimentum ante. In suscipit mollis lorem id commodo. Proin cursus ipsum sit amet odio mollis, sit amet consectetur arcu venenatis. Vivamus elementum magna id rhoncus ultrices. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse faucibus, sem quis posuere lobortis, nulla erat pretium lectus, et pellentesque turpis ligula ac neque. Donec quis sem varius leo volutpat ullamcorper. Nulla lobortis eu purus eu lacinia. Suspendisse non volutpat orci. Nullam euismod lectus elementum felis commodo sodales. Donec consectetur efficitur nunc, sit amet tincidunt ipsum maximus vitae. Quisque nec varius turpis.
    """

    new_msg = encrypt_msg(msg, 12)
    proof = """
    Xadqy ubegy paxad euf myqf, oazeqofqfgd mpubueouzs qxuf. Ymgdue eqp mzfq ymxqegmpm apua hqzqzmfue gxfduouqe eqp euf myqf zunt. Bqxxqzfqecgq tmnufmzf yadnu fduefucgq eqzqofge qf zqfge qf ymxqegmpm rmyqe mo fgdbue qsqefme. Mxucgmy qsqf mgsgq qxuf. Eqp uybqdpuqf mzfq rqxue. Zgxxm umogxue eqy nxmzpuf xunqda qsqefme, gf ogdege xqa xmouzum. Egebqzpueeq hufmq qj umogxue, adzmdq xqa cgue, baegqdq cgmy. Btmeqxxge qf qxqyqzfgy xunqda, ymffue moogyemz fgdbue. Bqxxqzfqecgq tmnufmzf yadnu fduefucgq eqzqofge qf zqfge qf ymxqegmpm rmyqe mo fgdbue qsqefme. Bdmqeqzf qzuy ymgdue, ruzunge eqp fuzoupgzf euf myqf, qsqefme mf yqfge. Mqzqmz eqp bgxhuzmd zgzo. Pgue qsqefme ymgdue uz qdae puszueeuy, xanadfue rduzsuxxm qdmf ymjuyge.

    Eqp uz qrruoufgd xadqy. Hqefungxgy bqxxqzfqecgq bdqfugy eapmxqe. Zgzo gf zunt mf xadqy hmduge badffufad. Zgxxmy eqy adou, ymjuyge euf myqf qgueyap mf, mxucgqf rmgounge zunt. Btmeqxxge gf qdae hufmq ymgdue rmgounge eapmxqe moogyemz qg apua. Eqp fgdbue fadfad, xmadqqf zqo embuqz mf, ymjuyge baegqdq ymszm. Adou hmduge zmfacgq bqzmfunge qf ymszue pue bmdfgduqzf yazfqe, zmeoqfgd dupuogxge yge. Zgxxmy ruzunge qxqyqzfgy yqfge zaz uybqdpuqf. Pazqo mxucgmy zueu hufmq xgofge ymffue. Btmeqxxge rmgounge ymszm qsqf pumy fduefucgq rduzsuxxm. Odme ymjuyge, hqxuf mf tqzpdqduf pmbunge, yu zgxxm oazhmxxue yu, cgue fduefucgq xunqda zgxxm eqp paxad. Bqxxqzfqecgq btmdqfdm ruzunge qzuy, zaz btmdqfdm xqa huhqddm hqx. Bdauz paxad vgefa, uzfqdpgy qsqf adou up, pmbunge huhqddm zgzo. Bdauz fuzoupgzf yu zaz xmoge adzmdq, mo btmdqfdm zgxxm moogyemz. Zgxxmy ymxqegmpm dgfdgy ymszm qg fuzoupgzf. Eqp eqp fqybad fqxxge.

    Mqzqmz badfm yqfge euf myqf ymgdue fduefucgq ymxqegmpm. Btmeqxxge rqgsumf, qdmf hufmq qxqurqzp pmbunge, zgxxm qdae qrruoufgd paxad, m tqzpdqduf qj ymeem cgue hqxuf. Btmeqxxge qzuy hqxuf, qsqefme cgue qj qg, bqxxqzfqecgq eaxxuoufgpuz fadfad. Zgxxmy bxmoqdmf, mgsgq cgue qxqyqzfgy mxucgqf, ymszm fqxxge hqtuogxm gdzm, gf emsuffue eqy eqy eqp qzuy. Zgzo qsqf xqa mo qdae bgxhuzmd fqybad xmouzum nxmzpuf paxad. Yadnu moogyemz ymjuyge haxgfbmf. Ymqoqzme qrruoufgd rmgounge yqfge zaz oazeqofqfgd. Ymqoqzme zgzo mzfq, eqybqd qf embuqz mo, btmdqfdm rmgounge zueu. Uz nxmzpuf xunqda nunqzpgy yqfge rqdyqzfgy eaxxuoufgpuz. Pgue mgofad eqp paxad qf huhqddm. Gf dtazoge paxad zaz mdog badffufad, hqx fduefucgq embuqz rduzsuxxm. Pazqo qsqf eqy rqxue. Pazqo mxucgqf xmadqqf fuzoupgzf.

    Uz tmo tmnufmeeq bxmfqm puofgyef. Hqefungxgy mzfq ubegy bduyue uz rmgounge adou xgofge qf gxfduoqe baegqdq ognuxum ogdmq; Qfumy qrruoufgd xanadfue vgefa, huhqddm fqybad duege emsuffue gxxmyoadbqd. Ymgdue gf mgsgq ymszm. Pazqo mxucgmy vgefa mf xmoge rqgsumf, hqx gxfduoqe ymeem qxqyqzfgy. Qfumy mo oazeqofqfgd pumy. Ymqoqzme gf qef huhqddm, ogdege apua zaz, pmbunge mzfq. Zgzo zaz mzfq pgu. Odme up fuzoupgzf vgefa, zqo gxfduouqe zqcgq. Pazqo eqp pgu mf ubegy huhqddm rmouxueue zaz gxxmyoadbqd fadfad. Eqp badffufad oazeqcgmf zueu, hqx rmouxueue bgdge uzfqdpgy eqp. Pazqo euf myqf zueu mgsgq. Egebqzpueeq euf myqf haxgfbmf qxuf, qsqf badffufad duege.

    Pazqo qg embuqz up xqa fqybad huhqddm. Zgzo gf uybqdpuqf xadqy, mo bqxxqzfqecgq cgmy. Uz hmduge yu haxgfbmf, tqzpdqduf qef m, qxqyqzfgy xusgxm. Ymgdue euf myqf xanadfue mdog, mo oazpuyqzfgy mzfq. Uz egeoubuf yaxxue xadqy up oayyapa. Bdauz ogdege ubegy euf myqf apua yaxxue, euf myqf oazeqofqfgd mdog hqzqzmfue. Huhmyge qxqyqzfgy ymszm up dtazoge gxfduoqe. Xadqy ubegy paxad euf myqf, oazeqofqfgd mpubueouzs qxuf. Egebqzpueeq rmgounge, eqy cgue baegqdq xanadfue, zgxxm qdmf bdqfugy xqofge, qf bqxxqzfqecgq fgdbue xusgxm mo zqcgq. Pazqo cgue eqy hmduge xqa haxgfbmf gxxmyoadbqd. Zgxxm xanadfue qg bgdge qg xmouzum. Egebqzpueeq zaz haxgfbmf adou. Zgxxmy qgueyap xqofge qxqyqzfgy rqxue oayyapa eapmxqe. Pazqo oazeqofqfgd qrruoufgd zgzo, euf myqf fuzoupgzf ubegy ymjuyge hufmq. Cguecgq zqo hmduge fgdbue.
    """
    assert proof == new_msg


def test_decrypt():
    text = "During the first part of your life, you only become aware of happiness once you have lost it. Then an age comes, a second one, in which you already know, at the moment when you begin to experience true happiness, that you are, at the end of the day, going to lose it. When I met Belle, I understood that I had just entered this second age. I also understood that I hadn’t reached the third age, in which anticipation of the loss of happiness prevents you from living."
    encrypted = "Pgduzs ftq rudef bmdf ar kagd xurq, kag azxk nqoayq mimdq ar tmbbuzqee azoq kag tmhq xaef uf. Ftqz mz msq oayqe, m eqoazp azq, uz ituot kag mxdqmpk wzai, mf ftq yayqzf itqz kag nqsuz fa qjbqduqzoq fdgq tmbbuzqee, ftmf kag mdq, mf ftq qzp ar ftq pmk, sauzs fa xaeq uf. Itqz U yqf Nqxxq, U gzpqdefaap ftmf U tmp vgef qzfqdqp ftue eqoazp msq. U mxea gzpqdefaap ftmf U tmpz’f dqmotqp ftq ftudp msq, uz ituot mzfuoubmfuaz ar ftq xaee ar tmbbuzqee bdqhqzfe kag rday xuhuzs."
    assert decrypt_msg_brute(encrypted, "words_alpha.txt") == text


def test_many_decrypts():
    text = "During the first part of your life, you only become aware of happiness once you have lost it. Then an age comes, a second one, in which you already know, at the moment when you begin to experience true happiness, that you are, at the end of the day, going to lose it. When I met Belle, I understood that I had just entered this second age. I also understood that I hadn’t reached the third age, in which anticipation of the loss of happiness prevents you from living."
    encrypted_texts = []
    for i in range(1, 27):
        encrypted_texts.append(encrypt_msg(text, i))
    for i in encrypted_texts:
        assert decrypt_msg_brute(i, "words_alpha.txt") == text
