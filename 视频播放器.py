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
