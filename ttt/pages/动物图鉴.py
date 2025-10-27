
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

