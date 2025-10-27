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

