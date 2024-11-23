import streamlit as st

x = 5
st.write('Hello \n COTAI:', x)  # joinable, same to print, one-line
st.write(f'Hello COTAI: {x}')
st.title('This is \n a title') # can't join, multi-line
st.header('This is a header')   # multi-line
st.subheader('This is a subheader') # multi-line
st.text('''This is a
multi-line\ntext''')   # multi-line
st.caption('This is \n a caption')  # one-line
st.divider()
st.code('x = 5\nprint(x)')  # multi-line
st.latex(r'x^2 + \sqrt{y} - z_{1} + \frac{1}{t} = \pi')    # one-line

st.title('Here is a Dog')
st.image('https://imgur.com/I4cxS4z.png')
st.subheader('Here are animals')
st.image('https://i.imgur.com/L3o3B9y.jpg')
st.text('Relax video')
st.video('https://youtu.be/PEDV27g-69s?si=0fTlyDblHT3bBvHD')

with st.sidebar:
    st.text('Dog in sidebar')
    st.image('https://static.streamlit.io/examples/dog.jpg')
st.title('Main window')
col1, col2 = st.columns(2)
with col1:
    st.text('Animals')
    st.image('https://as1.ftcdn.net/v2/jpg/06/69/69/42/1000_F_669694248_45qBxE5CTuL9jFSrD7ksgquIOatJkbx2.jpg')
with col2:
    st.text('Relax video')
    st.video('https://www.youtube.com/watch?v=M8C-oEs0uT0')

t1, t2 = st.tabs(["Um nha anh", "trong mit thai"])
with t1:
    st.image('https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/df6f9861-e02e-43a3-bfc8-f9a53f6e3b36/dg8zczz-99f2be43-189a-4d81-b1a7-19d6e6d47ca5.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcL2RmNmY5ODYxLWUwMmUtNDNhMy1iZmM4LWY5YTUzZjZlM2IzNlwvZGc4emN6ei05OWYyYmU0My0xODlhLTRkODEtYjFhNy0xOWQ2ZTZkNDdjYTUucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.5CP0Su4qTaSAFGAkwKMdAOXF-vitN5NcVR_JCiieof0')
    c1, c2 = st.columns(2)
    with c1:
        st.text('ok')
        st.image('https://math-media.byjusfutureschool.com/bfs-math/2022/07/04185628/Asset-1-8.png')
    with c2:
        st.title('i feel so sigma!')
    st.code('#typeshi')
with t2:
    st.image('https://i.pinimg.com/736x/ee/43/c7/ee43c703fffdbfac5a260e8372f2b2da.jpg')
    st.title('AFJDSKFLDSKJFDSAKLFKDJS')
    t3, t4, t5 = st.tabs([':)', ':(', ':/'])
    with t3:
        st.text('k')
    with t4:
        st.text('y')
    with t5:
        st.text('s')

st.divider()

text = st.text_input('Text input label', 'Python')
number = st.number_input('Number input label')
textarea = st.text_area('Text area label', '''Hello
COTAI''')

if st.button('OK'):
  st.write('text content:', text)
  st.write('number content:', number)
  st.text(textarea)

check = st.checkbox('Sport')
toggle = st.toggle('Music')
radio = st.radio('Radio', ('Option 1', 'Option 2', 'Option 3'))
# radio = st.radio('Radio', ('Option 1', 'Option 2', 'Option 3'), horizontal=True)

st.write('Check box:', check)
st.write('Toggle:', toggle)
st.write('Radio:', radio)

option = st.selectbox('Selectbox', ('select 1', 'select 2', 'select 3'))
multi = st.multiselect('Multiselect', ['Green', 'Yellow', 'Red', 'Blue'], ['Yellow', 'Red'])
slider = st.slider('Slider', 0, 130, 25)
day = st.select_slider('Select slider', options=['Monday', 'Tuesday', 'Wednesday', 'Friday', 'Saturday', 'Sunday'], value=['Monday', 'Wednesday'])

st.write('select box:', option)
st.write('multiselect:', multi)
st.write('slider:', slider)
st.write('select slider:', day)

st.divider()

st.title('Bé tập chơi đá')
c3, c4, c5 = st.columns(3)
with c3:
    a = st.number_input('a')
with c4:
    meth = st.radio('phep toan', ('\+', '\-', 'x', ':'))
with c5:
    b = st.number_input('b')
answ = st.number_input('nhap ket qua')
if st.button('kiem tra'):
    if meth == '\+':
        if a+b == answ:
            st.success('hay')
        else:
            st.error('ngu')
    elif meth == '\-':
        if a-b == answ:
            st.success('hay')
        else: st.error('ngu')
    elif meth == 'x':
        if a*b == answ:
            st.success('hay')
        else: st.error('ngu')
    elif meth == ':':
        if b == 0:
            st.warning('wtf negga')
            st.balloons()
        else:
            if a/b == answ:
                st.success('hay')
            else: st.error('ngu')
        
st.header(':3 ?')