import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os

st.set_page_config(
    page_title="学生成绩分析与预测系统",
    page_icon="📊",
    layout="wide"
)

# 保持原有函数不变
def get_sample_data():
    majors = ["计算机技术", "大数据管理与应用", "软件工程", "信息安全", "人工智能", "网络工程"]
    
    data = {
        "专业": majors,
        "每周平均学时": np.random.randint(15, 30, len(majors)),
        "期中考试平均分": np.random.randint(60, 85, len(majors)),
        "期末考试平均分": np.random.randint(65, 90, len(majors)),
        "男生比例": np.random.uniform(0.4, 0.8, len(majors)),
        "平均上课出勤率": np.random.uniform(0.7, 0.95, len(majors))
    }
    
    df = pd.DataFrame(data)
    df["女生比例"] = 1 - df["男生比例"]
    return df

# 修改模型训练函数，支持使用自定义数据集
def train_model(data=None):
    # 如果提供了数据，使用提供的数据；否则使用随机生成的数据
    if data is not None:
        # 假设数据集包含以下列：
        # 特征列：每周学习时长、出勤率、期中考试分数、作业完成率
        # 目标列：期末考试分数
        X = data[["每周学习时长", "出勤率", "期中考试分数", "作业完成率"]]
        y = data["期末考试分数"]
    else:
        # 生成随机数据作为备用
        np.random.seed(42)
        n_samples = 500
        
        study_hours = np.random.uniform(5, 40, n_samples)
        attendance = np.random.uniform(0.5, 1.0, n_samples)
        midterm_scores = np.random.randint(40, 100, n_samples)
        homework_completion = np.random.uniform(0.3, 1.0, n_samples)
        
        final_scores = 0.2 * study_hours + 15 * attendance + 0.5 * midterm_scores + 10 * homework_completion + np.random.normal(0, 5, n_samples)
        final_scores = np.clip(final_scores, 0, 100)  
        
        X = pd.DataFrame({
            "每周学习时长": study_hours,
            "出勤率": attendance,
            "期中考试分数": midterm_scores,
            "作业完成率": homework_completion
        })
        y = final_scores
    
    # 分割训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 训练模型
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # 评估模型
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    # 保存模型
    joblib.dump(model, "score_prediction_model.pkl")
    return model, mse, r2

def load_model():
    if os.path.exists("score_prediction_model.pkl"):
        return joblib.load("score_prediction_model.pkl")
    else:
        # 如果没有模型，使用默认数据训练
        model, _, _ = train_model()
        return model

# 保持原有页面函数不变
def page_introduction():
    st.title("🤣学生成绩分析和预测系统")
    
    st.markdown("---")
    
    st.header("😄这个的项目说明")
    st.write("""
    我们小组做的这个是一个基于Streamlit的学生成绩分析平台，用数据可视化还有机器学习技术，
    以及本次长达两周的课程的学习内容
    帮助教育工作者和学生深入了解学业表现，并预测期末考试成绩。
    """)
    
    st.subheader("一些特点：")
    st.markdown("""
    - 🍉数据可视化：多维度展示学生学业数据
    - 🍍专业分析：按专业分类的详细统计分析
    - 🍐智能预测：基于机器学习模型的成绩预测
    - 🍋学习建议：根据预测结果提供个性化反馈
    """)
    
    st.markdown("---")
    
    st.header("🗺️项目目标")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("目标一：分析影响因素")
        st.markdown("""
        - 识别学习指标
        - 探索成绩因素
        - 提供数据决策
        """)
    
    with col2:
        st.subheader("目标二：可视化展示")
        st.markdown("""
        - 专业对比分析
        - 性别差异研究
        - 学习模式识别
        """)
    
    with col3:
        st.subheader("目标三：成绩预测")
        st.markdown("""
        - 机器学习模型
        - 个性化预测
        - 及时干预预警
        """)
    
    st.markdown("---")
    
    st.header("🏟️技术架构")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.info("前端框架\nStreamlit")
    
    with col2:
        st.info("数据处理\nPandas\nNumPy")
    
    with col3:
        st.info("可视化\nPlotly\nMatplotlib")
    
    with col4:
        st.info("机器学习\nScikit-learn")

def page_major_analysis():
    st.title("😊 专业数据分析")
    
    df = get_sample_data()
    
    st.subheader("1. 各个专业学习数据统计")
    display_df = df[["专业", "每周平均学时", "期中考试平均分", "期末考试平均分", 
                    "平均上课出勤率"]].copy()
    display_df["平均上课出勤率"] = display_df["平均上课出勤率"].apply(lambda x: f"{x:.2%}")
    st.dataframe(display_df, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("2. 各个专业男女性别比例")
    gender_data = []
    for idx, row in df.iterrows():
        gender_data.append({"专业": row["专业"], "性别": "男生", "比例": row["男生比例"]})
        gender_data.append({"专业": row["专业"], "性别": "女生", "比例": row["女生比例"]})
    gender_df = pd.DataFrame(gender_data)

    fig = px.bar(
        gender_df,
        x="专业",
        y="比例",
        color="性别",
        barmode="stack", 
        color_discrete_map={"男生": "royalblue", "女生": "lightpink"},
        height=500
    )

    fig.update_layout(
        yaxis_title="比例",
        yaxis_tickformat=".0%",
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("3. 各个专业期中与期末考试分数对比")
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df["专业"],
        y=df["期中考试平均分"],
        mode='lines+markers',
        name='期中考试平均分',
        line=dict(color='royalblue', width=2)
    ))
    fig.add_trace(go.Scatter(
        x=df["专业"],
        y=df["期末考试平均分"],
        mode='lines+markers',
        name='期末考试平均分',
        line=dict(color='firebrick', width=2)
    ))
    
    fig.update_layout(
        yaxis_title="分数",
        yaxis_range=[0, 100],
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("4. 各专业平均上课出勤率")
    fig = px.bar(
        df,
        x="专业",
        y="平均上课出勤率",
        title="各专业平均上课出勤率",
        color="平均上课出勤率",
        color_continuous_scale="Blues",
        height=500
    )
    fig.update_layout(
        yaxis_title="出勤率",
        yaxis_tickformat=".0%"
    )
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("5. 大数据管理专业专项分析")
    big_data_df = df[df["专业"] == "大数据管理与应用"]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(
            "平均上课出勤率", 
            f"{big_data_df['平均上课出勤率'].values[0]:.2%}"
        )
        st.metric(
            "期末考试平均分", 
            f"{big_data_df['期末考试平均分'].values[0]:.1f}"
        )
    
    with col2:
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=["大数据管理专业"],
            y=[big_data_df["平均上课出勤率"].values[0]],
            name="平均上课出勤率",
            yaxis="y",
            marker_color='royalblue'
        ))
        fig.add_trace(go.Bar(
            x=["大数据管理专业"],
            y=[big_data_df["期末考试平均分"].values[0]],
            name="期末考试平均分",
            yaxis="y2",
            marker_color='firebrick'
        ))
        
        fig.update_layout(
    yaxis=dict(
        title=dict(
            text="出勤率",
            font=dict(color="royalblue")
        ),
        tickfont=dict(color="royalblue"),
        range=[0, 1.2],
        tickformat=".0%"
    ),
    yaxis2=dict(
        title=dict(
            text="分数",
            font=dict(color="firebrick")
        ),
        tickfont=dict(color="firebrick"),
        anchor="x",
        overlaying="y",
        side="right",
        range=[0, 100]
    ),
    height=300
)
        st.plotly_chart(fig, use_container_width=True)

# 修改成绩预测页面，增加数据集上传功能
def page_grade_prediction():
    st.title("🔮 期末成绩预测")
    
    # 数据集上传部分
    st.sidebar.subheader("模型训练设置")
    uploaded_file = st.sidebar.file_uploader("上传你的数据集 (CSV格式)", type=["csv"])
    
    # 显示模型状态
    if os.path.exists("score_prediction_model.pkl"):
        st.sidebar.success("已加载现有模型")
        if st.sidebar.button("重新训练模型"):
            if uploaded_file is not None:
                data = pd.read_csv(uploaded_file)
                with st.spinner("使用上传的数据训练模型中..."):
                    model, mse, r2 = train_model(data)
                    st.sidebar.success(f"模型训练完成！MSE: {mse:.2f}, R²: {r2:.2f}")
            else:
                with st.spinner("使用默认数据训练模型中..."):
                    model, mse, r2 = train_model()
                    st.sidebar.success(f"模型训练完成！MSE: {mse:.2f}, R²: {r2:.2f}")
    else:
        st.sidebar.info("尚未检测到模型，请上传数据并训练模型")
        if uploaded_file is not None and st.sidebar.button("使用上传数据训练模型"):
            data = pd.read_csv(uploaded_file)
            with st.spinner("训练模型中..."):
                model, mse, r2 = train_model(data)
                st.sidebar.success(f"模型训练完成！MSE: {mse:.2f}, R²: {r2:.2f}")
    
    # 显示上传的数据预览
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.subheader("上传的数据预览")
        st.dataframe(data.head(), use_container_width=True)
        
        # 检查数据格式是否符合要求
        required_columns = ["每周学习时长", "出勤率", "期中考试分数", "作业完成率", "期末考试分数"]
        missing_cols = [col for col in required_columns if col not in data.columns]
        
        if missing_cols:
            st.warning(f"上传的数据缺少必要的列：{', '.join(missing_cols)}")
            st.info("请确保你的数据集包含以下列：每周学习时长、出勤率、期中考试分数、作业完成率、期末考试分数")
    
    st.write("请输入学生的学习信息，系统将预测其期末考试成绩并提供学习建议")
    
    # 表单输入
    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            student_id = st.text_input("学号", "202123121")
            gender = st.selectbox("性别", ["男", "女"])
            major = st.selectbox("专业", ["计算机科学", "大数据管理", "软件工程", "信息系统", "人工智能", "网络工程"])
        
        with col2:
            study_hours = st.slider("每周学习时长(小时)", 0, 60, 15)
            attendance = st.slider("上课出勤率", 0.0, 1.0, 0.8, 0.01)
            midterm_score = st.slider("期中考试分数", 0, 100, 70)
            homework_completion = st.slider("作业完成率", 0.0, 1.0, 0.8, 0.01)
        
        submit_button = st.form_submit_button("预测期末成绩", use_container_width=True)
    
    if submit_button:
        # 检查模型是否存在
        if not os.path.exists("score_prediction_model.pkl"):
            st.warning("尚未训练模型，正在使用默认模型进行预测...")
        
        model = load_model()
        
        input_data = pd.DataFrame({
            "每周学习时长": [study_hours],
            "出勤率": [attendance],
            "期中考试分数": [midterm_score],
            "作业完成率": [homework_completion]
        })
        
        prediction = model.predict(input_data)[0]
        prediction = round(prediction, 1)
        
        st.markdown("---")
        st.subheader("预测结果")
        
        score_color = "green" if prediction >= 60 else "red"
        st.markdown(f"""
        <div style="background-color:#333; padding:10px; border-radius:5px; margin:10px 0;">
            <p style="color:white; margin:0;">预测期末成绩: <span style="color:{score_color}; font-size:24px; font-weight:bold;">{prediction}</span>/100</p>
        </div>
        """, unsafe_allow_html=True)
        
        if prediction >= 60:
            st.image("https://c8.alamy.com/comp/2F84FCF/keep-going-hand-drawn-motivation-lettering-phrase-for-poster-logo-greeting-card-banner-cute-cartoon-print-childrens-room-decor-vector-illustra-2F84FCF.jpg", 
                     caption="恭喜你！中大奖了")
            st.success("继续保持良好的学习状态，你已经走在正确的道路上！建议保持当前的学习节奏，适当复习薄弱环节。")
        else:
            st.image("https://img95.699pic.com/element/40263/9350.png_300.png", 
                     caption="让你玩摆烂，报应来里了吧。还有时间提升成绩！")
            st.warning("根据预测，你需要更加努力。建议增加学习时间，提高出勤率，及时完成作业，并重点复习期中考试中表现不佳的部分。")

def main():
    st.sidebar.title("导航菜单")
    page = st.sidebar.radio(
        "选择页面",
        ["项目介绍", "专业数据分析", "成绩预测"]
    )
    
    if page == "项目介绍":
        page_introduction()
    elif page == "专业数据分析":
        page_major_analysis()
    elif page == "成绩预测":
        page_grade_prediction()

if __name__ == "__main__":
    main()
