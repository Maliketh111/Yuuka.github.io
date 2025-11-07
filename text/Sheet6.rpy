define role1 = Character('?', color="#c8c8ff", image="role1")
define role2 = Character('我', color="#c8c8ff", image="role2")
define role3 = Character('林', color="#c8c8ff", image="role3")
define role4 = Character('母亲', color="#c8c8ff", image="role4")
define role5 = Character('医生', color="#c8c8ff", image="role5")
define narrator_nvl = Character(None, kind=nvl)
define narrator_adv = Character(None, kind=adv)
define config.voice_filename_format = "audio/{filename}"

label Sheet6:
scene wait2
play sound "audio/恋文.mp3"
narrator_adv "无疑，她的提议对我而言是不小的诱惑，但内心深处的声音似乎有点抗拒。"
scene background
narrator_adv "我看向山，黑色的山，连绵的山，静默无言的黑，与祭典是那么格格不入，不知为何此时竟有些亲近的感觉…"
scene background
narrator_adv "河，波光粼粼的河，人们在那里放着河灯，鱼儿时不时吐出几个泡泡，迅速升起，又立马化作泡影，归于虚无。"
scene background
narrator_adv "我又想起母亲的容颜，担心的，惊恐的，喜悦的，包容的…在我面前，她似乎从来没有展现过她懦弱的那一面。曾经模糊的脸庞，现在就连年岁的刻痕都在我眼前清晰浮现。"
scene background
narrator_adv "啊…那是小时候的我…笑的那么灿烂，可惜…现在的我大抵是再也不能像那样微笑了吧。"
scene background
narrator_adv " 过往的一切在我眼前一一浮现，曾经被掩盖的不可捉摸现在是那么的触手可得…"
scene wait2
narrator_adv " 视线被祭典的光牵扯回来，她依旧在那里站着，那么的美…"
scene wait2
role2 "“林，我…”"
scene pain
narrator_adv "我向她伸出手，正想开口，祭典的烟花突然升起，和吐出的泡泡一样又迅速归于虚无…"
scene pain
role3 " “我知道，我知道的哦”"
scene pain
narrator_adv "她轻声说到，泪流满面。虽然隔着一定距离，但她的声音还是清楚的传了过来。"
scene pain
narrator_adv "烟火转瞬即逝，一个消失又被另一个迅速替代，但终有落幕的时候，到最后橙光的烟火划过天空时，万物又归于那份如山的静默"
scene pain
role3 "“你已经，很坚强了呢…”"
scene pain
narrator_adv "她抬起手，拂过我的脸，但那只手从我的脸上穿了过去。"
scene pain
role3 "“该说再见了呢”"
scene pain
narrator_adv "“这段日子，我真的很开心…与你在一起的每一天都是那么多彩，那么让我流连忘返”"
scene pain
narrator_adv "“但是呢，终究，不能一直让你陪我到最后啊”"
scene pain
narrator_adv " 我想靠近她，当我抬起脚时，世界开始慢慢崩塌。"
scene byebye2
role3 "“再见，见到你真的很开心~”"
scene byebye2
narrator_adv "“对了，我叫林~”"
scene byebye2
narrator_adv "“一定要记住我哦~”"
scene background
narrator_adv " 白，布满天地的白，我只觉天旋地转，陷入晕厥…"
scene background
narrator_adv "…………"
scene background
narrator_adv "究竟是什么时候呢？"
scene background
narrator_adv "陌生的天花板，逐渐浮现在眼前"
scene background
narrator_adv "我缓缓抬起手，遮住刺眼的惨白的光线。"
scene background
narrator_adv "看向周围，仪器…各种各样的仪器，交织的各种杂音"
scene background
narrator_adv "“呼…呼…”"
scene background
narrator_adv "时快时慢的呼吸声，表明声音的主人睡的并不安稳。"
scene background
narrator_adv "那是我的母亲。"
scene background
role2 " “妈…妈…”"
scene background
narrator_adv "我哽咽着，视线逐渐模糊，轻声喊出这个让我心头一震的名字…"
scene background
narrator_adv " 她慢慢抬起头…熟悉的面庞，与我在祭典浮现的一模一样，那一道道皱纹，千沟万壑，刻在她的脸上，也在我的心上…"
scene background
role4 "“嗯…我在…我在…”"
scene background
narrator_adv "她颤抖着抬起手，抹去我眼角的泪。"
scene background
role2 "“妈妈…”"
scene background
narrator_adv "我抱紧她，感受着那份来之不易的温暖。"
scene background
narrator_adv "是啊……"
scene background
narrator_adv "纵使世界千疮百孔"
scene background
narrator_adv "纵使人生毫无希望"
scene background
narrator_adv "那个真正爱你的人，一直都在"
scene yuyi2
role3 "“千万，不能逃避哦。”"
scene background
narrator_adv "…………"
narrator_nvl "6月15日"
narrator_nvl "究竟是什么时候呢？"
narrator_nvl "日子一天天过着，和那些毫无意义的人打着交道，伪善地附和着他们…重复着重复着，毫无意义和价值。"
narrator_nvl "人是为什么活着呢？"
narrator_nvl "6月30日"
narrator_nvl "啊…看见他了"
narrator_nvl "一个人窝在房间里，难道不会很单调无聊嘛"
narrator_nvl "7月5日"
narrator_nvl "樱花树，很漂亮呢。"
narrator_nvl "樱花花瓣为什么那么轻呢？稍微一吹就全部飞走了…………"
narrator_nvl "好像多呆一会，和他一起………"
nvl clear
narrator_nvl "7月8日"
narrator_nvl "呼呼~他笨拙的样子，被我看到了哦"
narrator_nvl "原来不是只会板着脸嘛"
narrator_nvl "不过，买个菜都不敢还价……被欺负了怎么办"
narrator_nvl "算了，至少做菜还是很好吃的"
narrator_nvl "7月9日"
narrator_nvl "日记记得越来越勤了呢，明明不是很喜欢写东西"
narrator_nvl "为什么一天过得突然这么快呢？"
narrator_nvl "在公园坐了不到一会，太阳就从这头爬到那头了。"
narrator_nvl "7月20日"
nvl clear
narrator_nvl "真是的，隔了这么久才写一次日记……"
narrator_nvl "不知道为什么，看着日子一天天流逝，我好害怕"
narrator_nvl "7月21日"
narrator_nvl "温泉街？唔……好好奇"
narrator_nvl "他变得越来越好了呢"
narrator_nvl "哼哼，不愧是我看上的人"
narrator_nvl "7月25日"
narrator_nvl "温泉街真是至福啊…………那么多好吃的好玩的，烟花也好好看"
narrator_nvl "不过，是时候……告别了呢"
narrator_nvl "拜拜~"
narrator_nvl "…………"
nvl clear
narrator_nvl "如果……如果有机会的话"
narrator_nvl "我好想，好想告诉你啊"
narrator_nvl "再多陪我一会，一小会就好"
narrator_nvl "谁叫我……那么爱你嘛"
narrator_nvl "看着你不再逃避，我真的好开心好开心。"
narrator_nvl "一定要过的好好的哦"
narrator_nvl "不然……不然就再也不理你了！"
narrator_nvl "…………"
nvl clear
narrator_adv "达成结局： 好想亲口说出我爱你"
