import streamlit as st

st.title("广西职业师范学院")
tab1, tab2, tab3,tab4,tab5,tab6= st.tabs(["动物图鉴", "个人简历档案", "南宁美食","视频播放器","学生档案","音乐播放器"])

with tab1:
    
    import streamlit as st

    st.set_page_config(page_title='动物园', page_icon='🐒')

    # 图片数组
    images = [
    {   
        'url':'https://www.allaboutbirds.org/guide/assets/og/75712701-1200px.jpg',
        'parm':'鸟'
    },
    {   
        'url':'https://wallpapercave.com/wp/77vJ4jm.jpg',
        'parm':'狗'
    },     
    {   
        'url':'https://images2.alphacoders.com/716/71660.jpg',
        'parm':'猫'
    }
]

#将ind的值存储到seamlit的内存中，如果内存中没有ind，才要设置成0，否则不需要设置
    if'ind'not in st.session_state:
        st.session_state['ind']=0
#define:定义
    def nextImg():
        st.session_state['ind']=(st.session_state['ind']+1)%len(images)
    def lastImg():
        st.session_state['ind']=(st.session_state['ind']-1)%len(images)
#st.image()总共两个参数，url:图片地址 caption:图片的备注
    st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['parm'])
#将一行分成两列
    c1,c2=st.columns(2)
    with c1:
#st.button()按钮，text:按钮的文字，on_click:点击按钮之后要做的事情
      st.button('下一张',on_click=nextImg,use_container_width=True)
    with c2:
#st.button()按钮，text:按钮的文字，on_click:点击按钮之后要做的事情
      st.button('上一张',on_click=lastImg,use_container_width=True)


   

with tab2:
    import streamlit as st
    import datetime

# 页面配置
    st.set_page_config(
        page_title="个人简历生成器",
        layout="wide",
        initial_sidebar_state="collapsed"
)

# 标题
    st.title("个人简历生成器")
    st.caption("使用Streamlit创建你的个性化简历")

# 主布局：两列
    form_col, preview_col = st.columns([1, 1.2])

    with form_col:
    # 个人信息表单
        st.subheader("个人信息表单", anchor=False)
    
    # 基本信息
        st.markdown('<div class="form-section"><h4>基本信息</h4></div>', unsafe_allow_html=True)
        name = st.text_input("姓名", value="")
        position = st.text_input("职位", value="软件测试")
        phone = st.text_input("电话", value="18777765555")
        email = st.text_input("邮箱", value="23719311@qq.com")
        birthday = st.date_input("出生日期", datetime.date(2005, 6, 7))
    
    # 个人情况
        st.markdown('<div class="form-section"><h4>个人情况</h4></div>', unsafe_allow_html=True)
        gender = st.radio("性别", ["男", "女"], horizontal=True, index=0)
        education = st.selectbox("学历", ["本科", "专科", "高中", "硕士", "博士"], index=0)
    
    # 语言能力
        lang_options = ["中文", "英语", "日语", "韩语","泰语","俄语"]
        lang_selected = st.multiselect("语言能力", lang_options, default=["中文", "英语"])
        lang_display = [f"{lang} (熟练)" for lang in lang_selected]
    
    # 技能
        st.markdown('<div class="form-section"><h4>技能 (可多选)</h4></div>', unsafe_allow_html=True)
        skill_options = ["Java", "HTML/CSS", "Python", "SQL", "机器学习", "数据分析"]
        skills = st.multiselect("技能列表", skill_options, default=["Java", "HTML/CSS", "Python", "SQL"])
    
    # 工作经验与薪资
        st.markdown('<div class="form-section"><h4>求职信息</h4></div>', unsafe_allow_html=True)
        work_exp = st.slider("工作经验 (年)", 0, 30, 6)
    
    # 期望薪资范围
        min_salary, max_salary = st.slider(
        "期望薪资范围 (元)",
            5000, 50000, (32323, 28906)
    )
    
    # 最佳联系时间
        contact_time = st.text_input("最佳联系时间", value="09:41")
    
    # 个人简介
        st.markdown('<div class="form-section"><h4>个人简介</h4></div>', unsafe_allow_html=True)
        intro = st.text_area(
        "个人简介内容",
            height=120,
            value="1"
    )
    
    # 毕业院校
        st.markdown('<div class="form-section"><h4>教育背景</h4></div>', unsafe_allow_html=True)
        school = st.selectbox("毕业院校", ["每日科技技术学院", "其他院校","广西职业师范学院"], index=0)
    
    # 上传照片
        st.markdown('<div class="form-section"><h4>上传个人照片</h4></div>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "Drag and drop file here",
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=False
    )

    with preview_col:
    # 简历实时预览
        st.subheader("简历实时预览", anchor=False)
    
    # 姓名与基本信息
        st.markdown(f'<h2 class="preview-title">{name}</h2>', unsafe_allow_html=True)
    
    # 照片与基本信息布局
        info_top = st.columns([1, 3])
        with info_top[0]:
        # 显示上传的照片或默认头像
            if uploaded_file:
                st.image(uploaded_file, width=150)
            else:
            # 使用默认头像（可替换为实际图片URL）
                st.image("https://picsum.photos/200/200", width=150)
    
        with info_top[1]:
        # 右侧基本信息
            st.write(f"**职位:** {position}")
            st.write(f"**电话:** {phone}")
            st.write(f"**邮箱:** {email}")
            st.write(f"**出生日期:** {birthday.strftime('%Y-%m-%d')}")
    
    # 个人信息网格
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="info-grid">', unsafe_allow_html=True)
        st.write(f"**性别:** {gender}")
        st.write(f"**学历:** {education}")
        st.write(f"**工作经验:** {work_exp}年")
        st.write(f"**期望薪资:** {min_salary}-{max_salary}元")
        st.write(f"**最佳联系时间:** {contact_time}")
        st.write(f"**语言能力:** {', '.join(lang_display)}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # 个人简介
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        st.subheader("个人简介", anchor=False)
        st.write(intro)
    
    # 专业技能
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        st.subheader("专业技能", anchor=False)
        skill_html = ''.join([f'<span class="skill-tag">{skill}</span>' for skill in skills])
        st.markdown(skill_html, unsafe_allow_html=True)
    
    # 毕业院校
        st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
        st.write(f"**毕业院校:** {school}")

# 底部操作按钮
    st.write("---")
    col_btn1, col_btn2 = st.columns([1, 1])
    with col_btn1:
        st.button("保存信息")
    with col_btn2:
        st.button("生成PDF简历", type="primary")

with tab3:
    import streamlit as st
    import pandas as pd
    import numpy as np
    data={
    '嗨老友club':[568,868,670,884,144,300,150,280,759,965,658,459],
    '巨星livehouse':[577,532,996,926,694,568,868,670,884,144,459,785],
    'HEY BABE CLUB':[577,532,996,926,694,577,532,996,926,694,659,876],
    'COMMUNE幻师':[120,168,123,568,752,577,532,996,926,694,784,985],
    'zeta酒吧':[300,150,280,759,965,577,532,996,926,694,748,459],
    }
# 将字典转换为DataFrame数据框
    df=pd.DataFrame(data)
# 创建一个Series作为索引，包含1-12月，命名为"月份"
    index=pd.Series(['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月'],name='月份')
# 将创建的月份索引设置为DataFrame的行索引
    df.index=index
# 在页面上显示交互式数据框
    st.dataframe(df)
# 在页面上显示静态表格（不支持交互）
    st.table(df)
# 以折线图形式展示数据（x轴为月份，y轴为数值，每条线代表一个场所
    st.line_chart(df)
# 以柱状图形式展示数据（x轴为月份，y轴为数值，每组柱子代表一个月份的各场所数据）
    st.bar_chart(df)
# 定义一个新字典，存储场所名称及对应的经纬度信息
    data = {
        '场所名称': ['嗨老友club', '巨星livehouse', 'HEY BABE CLUB', 'COMMUNE幻师', 'zeta酒吧'],
        'latitude': [22.810370, 22.830402, 22.806038, 22.847441, 22.786225],  # 纬度列（列名符合要求）
        'longitude': [108.399090, 108.390963, 108.375543, 108.320796, 108.305840]  # 经度列（列名符合要求）
}
# 将经纬度数据转换为DataFrame
    df = pd.DataFrame(data)
# 在页面上显示地图，根据经纬度标注各个场所的位置
    st.map(df)
with tab4:
    import streamlit as st

    st.set_page_config(page_title='视频播放器',page_icon='🐒')

#视频地址

    video_url=[{
                'url':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/10/38/33347603810/33347603810-1-192.mp4?e=ig8euxZM2rNcNbRM7bdVhwdlhWKjhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1761301891&oi=771356656&nbs=1&uipk=5&gen=playurlv3&os=cosovbv&og=cos&platform=html5&trid=37e6ed3e359444bc8652ab7779b2c38h&mid=0&upsig=80c71fa64ab0250baed42d88048f706f&uparams=e,deadline,oi,nbs,uipk,gen,os,og,platform,trid,mid&bvc=vod&nettype=0&bw=1172774&build=0&dl=0&f=h_0_0&agrr=1&buvid=&orderid=0,1',
                'title':'NBA库里',
                'episode':'1'
            },
         {
                'url':'https://upos-sz-mirrorbd.bilivideo.com/upgcxcode/19/64/30962616419/30962616419-1-192.mp4?e=ig8euxZM2rNcNbNz7zdVhwdlhbhahwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&oi=1782024106&deadline=1761303388&nbs=1&trid=a510f4fda29849c0bbe44ffd1e52016h&mid=0&gen=playurlv3&os=bdbv&og=hw&uipk=5&platform=html5&upsig=b4c1ce692e982da6a42b45385531cfa2&uparams=e,oi,deadline,nbs,trid,mid,gen,os,og,uipk,platform&bvc=vod&nettype=0&bw=1898632&build=0&dl=0&f=h_0_0&agrr=1&buvid=&orderid=0,1',
                'title':'NBA库里',
                'episode':'2'
            },
         {
                'url':'https://upos-sz-estgcos.bilivideo.com/upgcxcode/70/50/1549545070/1549545070-1-192.mp4?e=ig8euxZM2rNcNbNMnWdVhwdlhbKHhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1761303554&uipk=5&platform=html5&mid=0&nbs=1&oi=1782024106&os=estgcos&trid=bad2f92de31443c19ce0ff9c08032d2h&gen=playurlv3&og=cos&upsig=334be207ce594f0703ce1e4c9a567b07&uparams=e,deadline,uipk,platform,mid,nbs,oi,os,trid,gen,og&bvc=vod&nettype=0&bw=2002731&buvid=&build=0&dl=0&f=h_0_0&agrr=1&orderid=0,1',
                'title':'NBA库里',
                'episode':'3'
            }
    ]

    if'ind' not in st.session_state:
        st.session_state['ind']=0


    st.title(video_url[st.session_state['ind']]['title']+'-第'+video_url[st.session_state['ind']]['episode']+'集')
    st.video(video_url[st.session_state['ind']]['url'])

    c1, c2, c3=st.columns(3)

    def play(arg):
    #将传递过来的值，赋值给内存中的ind
      st.session_state['ind']=int(arg)

    for i in range(len(video_url)):
        st.button('第'+str(i+1)+'集',use_container_width=True,on_click=play,args=([i]))
     

with tab5:
    import streamlit as st

    import pandas as pd

    from datetime import datetime



# 主标题

    st.title("🕶️ 学生 小陆 - 数字档案")



# 基础信息章节

    st.header("🔑 基础信息")

    st.text("学生ID: NEO-2023-001")

    st.markdown("**注册时间**: `2023-10-01 08:30:17` | **精神状态**: ✅ 正常")

    st.markdown("**当前教室**: `实训楼301` | **安全等级**: `绝密`")



# 技能矩阵章节

    st.header("📊 技能矩阵")

    col1, col2, col3 = st.columns(3)

    col1.metric("C语言", "95%", "2%", help="近期训练提升") 

    col2.metric("Python", "87%", "-1%")

    col3.metric("Java", "68%", "-10%", help="用则进废则退")



# 进度条展示

    st.subheader("Streamlit课程进度")

    st.progress(28, text="Streamlit课程进度")



# 任务日志章节

    st.header("📝 任务日志")

    mission_data = {

        "日期": ["2023-10-01", "2023-10-05", "2023-10-12"],

        "任务": ["学生数字档案", "课程管理系统", "数据图表展示"],

        "状态": ["✅ 完成", "🕒 进行中", "❌ 未完成"],

        "难度": ["★☆☆☆☆", "★★☆☆☆", "★★★☆☆"]

}

    mission_df = pd.DataFrame(mission_data)

    st.table(mission_df.style.applymap(

        lambda x: 'color: #0f0' if x == "✅ 完成" else 'color: #ff0')

)



# 代码块展示

    st.subheader("🔐 最新代码成果")

    st.code('''def matrix_breach():

        while True:

            if detect_vulnerability():

                exploit()

                return "ACCESS GRANTED"

            else:

                stealth_evade()''', language='python')



# 动态信息流

    st.write("---")

    st.write("`>> SYSTEM MESSAGE:` 下一个任务目标已解锁...")

    st.write("`>> TARGET:` 课程管理系统")

    st.write("`>> COUNTDOWN:`", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

with tab6:
    import streamlit as st

    st.set_page_config(page_title='音乐播放器',page_icon='🐒')

# 创建一个标题展示元素，内容是全中文的
# 如不定义anchor参数，则无锚点
    st.title("🎧️简易音乐播放器")

# 第一个普通文本展示元素，无工具提示
    st.text("使用Streamlit制作的简单音乐播放器，支持切歌和基本播放控制")


    # 图片数组
    images = [
        {
                'url':'https://music.163.com/song/media/outer/url?id=2526625.mp3',
                'author':'Deep Side',
                'photo':'https://p1.music.126.net/dUSiZ5ASRpWgaq9OTMtoDw==/860917604602698.jpg?param=250y250'
            },
         {
                'url':'https://music.163.com/song/media/outer/url?id=175072.mp3',
                'author':'夏天',
                'photo':'https://p1.music.126.net/1IyS4hDwsxgzIObfQU5__g==/71468255818380.jpg?param=250y250'
            },
         {
                'url':'https://music.163.com/song/media/outer/url?id=191248.mp3',
                'author':'张杰',
                'photo':'https://p2.music.126.net/ixIs5kkukgNYMmeDsc35_g==/29686813955450.jpg?param=250y250'
            }
    ]
           

#将ind的值存储到streamlit的内存中，如果内存中没有ind，才要设置成0，否则不需要设置
    if 'ind' not in st.session_state:
        st.session_state['ind']=0


#define:定义
    def nextImg():
        st.session_state['ind']=(st.session_state['ind']+1)%len(images)
    def lastImg():
        st.session_state['ind']=(st.session_state['ind']-1)%len(images)


    b1,b2=st.columns(2)
    with b1:
    # st.image()总共两个参数，url：图片地址 caption:图片的备注
        st.image(images[st.session_state['ind']]['photo'])


    with b2:
       st.text(images[st.session_state['ind']]['author'])
   #将一行分成两列
       c1,c2 = st.columns(2)

       with c1:
    #st.button()按钮，text:按钮的文字，on_click:点击按钮之后要做的事情
        st.button('上一首',on_click=lastImg,use_container_width=True)
    
       with c2:
    #st.button()按钮，text:按钮的文字，on_click:点击按钮之后要做的事情
        st.button('下一首',on_click=nextImg,use_container_width=True)

    st.audio(images[st.session_state['ind']]['url'])


