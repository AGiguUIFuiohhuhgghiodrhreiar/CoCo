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
