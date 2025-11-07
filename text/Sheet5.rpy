define role1 = Character('?', color="#c8c8ff", image="role1")
define role2 = Character('我', color="#c8c8ff", image="role2")
define role3 = Character('林', color="#c8c8ff", image="role3")
define role4 = Character('母亲', color="#c8c8ff", image="role4")
define role5 = Character('医生', color="#c8c8ff", image="role5")
define narrator_nvl = Character(None, kind=nvl)
define narrator_adv = Character(None, kind=adv)
define config.voice_filename_format = "audio/{filename}"

label Sheet5:
scene wait2
narrator_adv "经过一番思想挣扎，我逐渐放弃，她十分完美，符合我所有想象，沉湎于温柔有什么不好？我抱住她，轻轻点了点头。"
scene wait2
role3 "“好哦，那就一直，一直在一起~”"
scene wait2
narrator_adv "她温柔的回答道，眼中带着难以察觉的失望，但很快被激动与狂喜所替代…"
scene background
narrator_adv "…………"
scene background
narrator_adv " 滴嘟…滴嘟…"
scene background
narrator_adv "刺耳的仪器声，在某家医院的病床前，母亲趴在床前，面容憔悴…"
scene background
narrator_adv " 滴——"
scene background
narrator_adv " 诡异的声音划破焦躁的空气，仪表上的心跳瞬间归零，变成一条可怕的直线。"
scene background
narrator_adv "  杂乱的脚步声由远及近，医生们推走病床上的我，开始紧急抢救，母亲在急救室前，焦急的搓着手。"
scene background
role5 "“抱歉，请您节哀”"
scene background
narrator_adv "经过几个小时的抢救，主治医生走出急救室。"
scene background
narrator_adv "他拍了拍母亲的肩，然后离开，后面跟着被白布盖着的我。"
scene background
narrator_adv " 听到这句话的一瞬，仿佛失去所有力气，母亲倒在地上，眼睛布满红血丝，无声的，无泪的哭泣。"
scene background
narrator_adv "达成结局：happy…ending？"
