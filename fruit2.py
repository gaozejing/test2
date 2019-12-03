import easygui
Name = easygui.enterbox("姓名：")
Room = easygui.enterbox("房间号：")
Street = easygui.enterbox("街道：")
City = easygui.enterbox("城市：")
Number = easygui.enterbox("邮政编码：")
easygui.msgbox(Name+Room+Street+City+Number)