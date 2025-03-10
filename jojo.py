import streamlit as st
st.title('JOJO')
st.image('joojo.png')
st.title('Resumo básico de cada protagonista/vilão ')
tab1, tab2 = st.tabs(['protagonistas', 'vilões'])
with tab1:
    tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(['johnathan joestar', 'joseph joestar', 'jotaro kujo', 'josuke higashikata', 'giorno giovana', 'jolyne kujo', 'johnny joestar', 'gappy'])
    with tab3:
        st.image('johnathan2.png')
        st.markdown('## Jonathan Joestar (ジョナサン・ジョースター Jonasan Jōsutā) é o protagonista de Phantom Blood e o primeiro JoJo da série JoJo`s Bizarre Adventure.Filho de George Joestar I, Jonathan é um homem honesto, gentil e positivo, cuja vida está repleta de tragédias após conhecer seu irmão mais velho adotivo, Dio Brando. Em sua batalha contra Dio, Jonathan se torna um usuário do Hamon sob a tutela de Will Anthonio Zeppeli.')
    with tab4:
        st.image('joseph2.png')
        st.markdown('''
                    ## Joseph Joestar (ジョセフ・ジョースター Josefu Jōsutā) é o protagonista de Battle Tendency e um aliado em Stardust Crusaders e Diamond is Unbreakable. Ele é o segundo JoJo da série JoJo's Bizarre Adventure. Ele também é o segundo JoJo mais recorrente da série depois de seu neto Jotaro Kujo e é um de seus personagens mais conhecidos.
                    ''')
    with tab5:
        st.image('jotaro2.png')
        st.markdown('''
                    ## Jotaro Kujo (空条 承太郎 Kūjō Jōtarō) é o protagonista da Parte 3 e também aparece nas Partes 4-6 Jotaro é o terceiro e o JoJo mais recorrente na série JoJo's Bizarre Adventure.

### Jotaro é um delinquente que vive uma vida normal até que o velho inimigo da Família Joestar, DIO, retorna. Jotaro viaja para o Egito para salvar sua mãe e parar o Vampiro de uma vez por todas.'''
                    )