define role1 = Character('?', color="#c8c8ff", image="role1")
define role2 = Character('我', color="#c8c8ff", image="role2")
define role3 = Character('林', color="#c8c8ff", image="role3")
define role4 = Character('母亲', color="#c8c8ff", image="role4")
define role5 = Character('医生', color="#c8c8ff", image="role5")
define narrator_nvl = Character(None, kind=nvl)
define narrator_adv = Character(None, kind=adv)
define config.voice_filename_format = "audio/{filename}"

label Sheet3:
scene background
narrator_adv "想想还是算了，我回头看向房间里熟悉的黑暗，林呢？这是我第一次那么想见到她…"
scene background
narrator_adv " 不过我很快打消这个念头，已经…不能依靠任何人了啊…"
scene background
narrator_adv " 别扭着穿好浴衣，我出门了"
scene background
narrator_adv "……"
scene yuyi
play sound "audio/花鸟风月.mp3"
narrator_adv " 打开门，林早已穿好浴衣等待着我，群山下是橙黄灯火的温泉街，祭典的鼓声随着远处芦之湖的波光传来，一切的一切似乎都在为她做映衬，美艳不可方物。"
scene doki
role3 " “怎么，看呆啦，呆瓜~”"
scene doki
narrator_adv "她看着我，笑颜如花。"
scene doki2
role3 "“快走啦，再慢点赶不上祭典了哦~”"
scene doki2
narrator_adv "她牵起我的手，向温泉街奔去。"
scene street（dark）
narrator_adv " 一路的车水马龙在我眼前飞速流逝，几乎瞬间，我便来到温泉街前。"
scene street（dark）
narrator_adv "祭奠的一切熟悉又陌生，她似乎有用不完的精力，从东向西，从南向北，逛完每个摊位。"
scene play
role3 "“快看快看，有金鱼~”"
scene eat2
narrator_adv "“哇，这个好好吃，我想要~”"
scene shoot
narrator_adv "“快走啦~前面还有好玩的”"
scene background
narrator_adv "…………"
scene wait
narrator_adv "  一路拉拉扯扯，我们来到山顶，她靠在栏杆边，默默的看着我"
scene wait2
narrator_adv "不同以往的古灵精怪，这次，她的眼睛似乎在颤抖，波光流转，无奈，不舍，欣慰。各种各样的情绪从她眼里流出，不知为何，我开始紧张起来。"
scene wait2
role3 "“你愿意…一直陪着我嘛”"
scene wait2
narrator_adv "“一直，一直在一起，只有我们两个人”"
scene wait2
narrator_adv "她一边说着，一边靠近我，缓缓地将我环抱住"
scene wait2
role3 "“好不好嘛…求求你”"
scene wait2
narrator_adv "她在我耳边呢喃，吐气如兰，带着无尽的央求和诱惑…"
scene wait2
role3 "“难道……难道这样不快乐嘛，我可以满足你的任何要求哦”"
scene wait2
narrator_adv "我逐渐难以招架，但母亲的动作，眼睛，神情逐渐浮现在眼前，我…"
menu:
    "答应她":
        jump Sheet5

    "拒绝她":
        jump Sheet6
