import streamlit as st

st.header("🐙 Team")

Faculty, Postdocs, Students = st.tabs(['Faculty', 'Postdocs', 'Students'])

with Faculty:
    with st.expander("Saurabh Khanna", expanded = True):
        st.image("images/saurabh_khanna.jpg", caption="saurabh.khanna@uva.nl", width=200)
        st.write("""
                Saurabh Khanna is an Assistant Professor in Communication Science at the University of Amsterdam, and a Research Fellow at the University of Oxford. He leverages machine learning and information retrieval to study the diversity and limits of human knowledge in an increasingly digitized world. Saurabh received his PhD in education policy and computer science from Stanford University, where he was a Human-centered AI Fellow, a Stanford Data Science Scholar, and a William R and Sara Hart Kimball Fellow. His prior background spans computer science engineering (BITS Pilani), economics (Stanford), and education (TISS). More [here](https://saurabh-khanna.github.io/).
            """)

    with st.expander("Olga Eisele", expanded = True):
        st.image("images/olga_eisele.jpeg", caption="o.eisele@uva.nl", width=200)
        st.write("""
                Olga Eisele is an Assistant Professor in the Corporate Communication Program Group at the Amsterdam School of Communication Research (ASCoR). Before joining ASCoR in 2022, she held positions at the Institute for Advanced Studies in Vienna, Austria, as well as the University of Siegen, Germany. After completing her PhD at Vienna University in 2017, she was Principal Investigator of two research projects on political-media dynamics in times of crisis with a special focus on the European Union. Her research has been published in the European Journal of Political Research , European Union Politics, Journal of Common Market Studies, Political Communication, and Communication Methods & Measures.
            """)

    with st.expander("Chei Billedo", expanded = True):
        st.image("images/chei_billedo.jpg", caption="c.j.billedo@uva.nl", width=200)
        st.write("""
                Cherrie Joy (Chei) F. Billedo (PhD, VU University) is an Assistant Professor in Youth and Media Entertainment at the University of Amsterdam, Amsterdam School of Communication Research (ASCoR). Her research interests include representation in media science, social media use among minoritized social groups, and media representation effects among young people.
            """)

    with st.expander("Britta Brugman", expanded = True):
        st.image("images/britta_brugman.jpg", caption="b.c.brugman@uva.nl", width=200)
        st.write("""
                Britta Brugman is an Assistant Professor in Communication Science at the University of Amsterdam. Her research focuses on the characteristics of moralising communication and its effects on public opinion formation across various communication contexts: satire, journalism, and communication by and about organisations.
            """)

    with st.expander("Sandra Jacobs", expanded = True):
        st.image("images/sandra_jacobs.jpg", caption="s.h.j.jacobs@uva.nl", width=200)
        st.write("""
                Sandra Jacobs (PhD, Utrecht University, School of Governance) is Assistant Professor in Corporate Communication at the University of Amsterdam, Amsterdam School of Communication Research (ASCoR), the Netherlands. In her research, she focuses on strategic communication of organizations, mediatization, and the mediated construction of societal debates.
            """)

    with st.expander("Corine Meppelink", expanded = True):
        st.image("images/corine_meppelink.jpg", caption="c.s.meppelink@uva.nl", width=200)
        st.write("""
                Corine Meppelink (PhD, University of Amsterdam) is an Assistant Professor of Persuasive Communication (UvA, ASCoR). Her research focuses on inequalities in the digital society caused by literacy differences (e.g., health literacy, digital literacy) and persuasion through new media technologies.
            """)
        
    with st.expander("Lauren Taylor", expanded = True):
        st.image("images/lauren_taylor.jpg", caption="l.b.taylor@uva.nl", width=200)
        st.write("""
                Lauren B. Taylor (PhD, University of California, Davis) is a Lecturer in Youth and Media Entertainment and ASCoR Associate Member at the University of Amsterdam. Her research interests include social media use of children and adolescents with varying mental health and developmental needs, effects of exposure to social media influencers, and authentic media representation and implications for mental health.
            """)
        

    with st.expander("Marina Tulin", expanded = True):
        st.image("images/marina_tulin.jpg", caption="m.tulin@uva.nl", width=200)
        st.write("""
                Marina Tulin (PhD, UvA) is an Assistant Professor in Political Communication & Journalism as well as in the sector theme Education, Citizenship and Democracy in a Digital World. She conducts research on mis- and disinformation, fact-checking, media literacy and public trust in institutions like journalism and science.
            """)

with Postdocs:
    with st.expander("Marieke van Hoof", expanded = True):
        st.image("images/marieke_van_hoof.jpeg", caption="m.vanhoof@uva.nl", width=200)
        st.write("""
                Marieke van Hoof is a PhD Student in Political Communication, and will soon start as a postdoctoral researcher within the FMG faculty's Research Priority Area “Artificial Intelligence & Politics.” Her research primarily explores how digital information environments and their underlying algorithms shape the public's access to political information. In her research, she combines computational and traditional data collection and analysis methods.
            """)
        
with Students:
    with st.expander("Daniela An", expanded = True):
        st.image("images/daniela_an.jpg", caption="daniela.an@student.uva.nl", width=200)
        st.write("Jaemin Daniela An is a Research Master student in Communication Science at the University of Amsterdam, Amsterdam School of Communication Research (ASCoR). Her research interests focus on new media technologies such as immersive media and human-machine communication.")
    with st.expander("Iria Cheng", expanded = True):
        st.image("images/iria_cheng.jpg", caption="iria.a.cheng@student.uva.nl", width=200)
        st.write("Huiwen (Iria) Cheng is currently a second year Research Master student at University of Amsterdam. She completed her bachelor's degree in Journalism, motivated by a passion for promoting social justice. She also developed expertise in qualitative research methods, sparking interest in social issues, especially those surrounding gender (in)equality. During her Master's program at UvA, Cheng gained experience in both quantitative and qualitative research, and is eager to advance computational communication skills. She hopes to understand and interpret the society better, through the lens of data-driven insights. And, she is now taking strides into the vast field of life! P.S. She is also a good-food lover, an explorer of different music genres, and an enthusiast for philosophy books, tennis, and Lego!")
    with st.expander("Xiwen Duan", expanded = True):
        st.image("images/xiwen_duan.jpeg", caption="xiwen.duan@student.uva.nl", width=200)
        st.write("Xiwen Duan is currently pursuing a Research Master's in Communication Science at the University of Amsterdam, with a particular passion for digital analytics and digital health marketing, focusing on sensory technology. I completed my Bachelor in Communication Science at the University of Amsterdam. In my free time, I enjoy playing squash, dancing (especially Zumba), and catching up on sleep.")
    with st.expander("Xinkangrui Gao", expanded = True):
        st.image("images/xingkangrui_gao.png", caption="xinkangrui.gao@student.uva.nl", width=200)
        st.write("Xinkangrui Gao is a Research Master’s student in Communication Science at the University of Amsterdam. She completed her undergraduate studies in Communication at Fudan University. Her research interests include health information, misinformation, and human-computer interaction.")
    with st.expander("Qianyi Wang", expanded = True):
        st.image("images/qianyi_wang.jpeg", caption="qianyi.wang@student.uva.nl", width=200)
        st.write("Qianyi Wang is a Research Master student in Communication Science at the University of Amsterdam. Her academic journey has been not only intellectually but also personally transformative. The transition involves moving to the Netherlands as a late teenager, being face-to-face with a world very different from the one in which she grew up, which shaped her perspective on identity, culture, and representation. Her research focuses on the ways Western mainstream media portray marginalized groups and cultures, the impact of media representation on young generations' identity and psychological development, and the broader effects these have on societal well-being. She believes these questions are essential to advancing our understanding of human connection and social progress.")
    with st.expander("Yuetong Wu", expanded = True):
        st.image("images/yuetong_wu.jpeg", caption="yuetong.wu@student.uva.nl", width=200)
        st.write("Yuetong Wu is a Research Master’s student in Communication Science at the University of Amsterdam (UvA), with a background in Advertising from Zhejiang University. Her research interests include strategic communication online (health, advertising) and media representation online.")
    with st.expander("Jiayi Yan", expanded = True):
        st.image("images/jiayi_yan.jpg", caption="jiayi.yan2@student.uva.nl", width=200)
        st.write("Jiayi Yan is a Research Master Student in Communication Science at the University of Amsterdam. With a background in linguistics and media studies, her research focuses on social (digital) activism, intersectionality in feminist studies, and the media representation of minoritized social groups.")
    
