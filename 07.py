#第八章/atreamlit_predict_05.py
import streamlit as st
import pickle
import pandas as pd
#设置页面标题、图标和分布
st.set_page_config(
    page_title="企鹅分布器",#页面标题
    page_icon=":penguin:",#页面图标
    layout='wide')
#使用侧边栏实现多页面显示效果
with st.sidebar:
    st.image('D:/images/rigth_logo.png',width=100)
    st.title('请选择页面')
    page=st.selectbox("请选择页面",["简介页面","预测分类页面"],label_visibility='collapsed')

if page=="简介页面":
    st.title("企鹅分类器:penguin:")
    st.header('数据集介绍')
    st.markdown("""帕尔默群岛企鹅数据集是用于数据探索和数据可视化的一个出色的数据集，也可以作为机器学习入门练习。
                       该数据集是由Gorman等收集，并发布在一个名为palmerpengguins的R语言包，以对南极企鹅种类进行分类和研究。
                       该数据记录了344行观测数据，包含了3个不同物种的企鹅：阿德利企鹅、巴布亚企鹅和带帽企鹅的各种信息。""")
    st.header('三种企鹅的卡图像')
    st.image('D:/images/penguins.png')

elif page=="预测分类页面":
    st.header("预测企鹅分类")
    st.markdown("这个web应用是基于帕尔默群岛企鹅数据集构建的模型。只需输入6个信息，就可以预测企鹅的物种，使用下面的表单开始预测吧！")
    #该页面布局是3:1:2的列布局
    col_form,col,col_logo=st.columns([3,1,2])
    with col_form:
        #运用表单和表单提交按钮
        with st.form('user_inputs'):
            island=st.selectbox('企鹅栖息的岛屿',
                                    options=['托尔斯森岛', '比斯科群岛', '德里岛'])
            sex = st.selectbox('性别', options=['雄性', '雌性'])
                
            bill_length = st.number_input('喙的长度（毫米）', min_value=0.0)
            bill_depth = st.number_input('喙的深度（毫米）', min_value=0.0)
            flipper_length = st.number_input('翅膀的长度（毫米）', min_value=0.0)
            body_mass = st.number_input('身体质量（克）', min_value=0.0)
            submitted = st.form_submit_button('预测分类')
            island_biscoe, island_dream, island_torgerson = 0, 0, 0
            if island == '比斯科群岛':
                    island_biscoe = 1
            elif island == '德里岛':
                island_dream = 1
            elif island == '托尔斯森岛':
                island_torgerson = 1
            sex_male,sex_female=0,0
            if sex == '雌性':
                sex_female = 1
            elif sex == '雄性':
                sex_male = 1
            format_data = [bill_length, bill_depth, flipper_length, body_mass,
                            island_dream, island_torgerson, island_biscoe, sex_male, sex_female ]
            with open('rfc_model.pkl', 'rb') as f:
                rfc_model = pickle.load(f)
            with open('output_uniques_map.pkl', 'rb') as f:
                output_uniques_map = pickle.load(f)

            if submitted:
                format_data_df = pd.DataFrame(data=[format_data], columns=rfc_model.feature_names_in_)
                predict_result_code = rfc_model.predict(format_data_df)
                predict_result_species = output_uniques_map[predict_result_code[0]]
                st.write(f"根据您输入的数据，预测该企鹅的物种名称是：**{predict_result_species}**")
            with col_logo:
                if not submitted:
                    st.image('D:/images/rigth_logo.png', width=300)
                else:
                    st.image('D:/images/rigth_logo.png', width=300)



                    


                    

                    
