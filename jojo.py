import streamlit as st
st.title('JOJO')
st.image('joojo.png')
st.title('Biografia básica de cada protagonista/vilão ')
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
    with tab6:
        st.image('josuke.png')
        st.markdown('''
        ## Josuke Higashikata (東方 仗助, Higashikata Jōsuke; o Suke — 助 — em seu nome também pode ser pronunciado como "Jo") é o protagonista de Diamond is Unbreakable e o quarto JoJo da série série JoJo's Bizarre Adventure.

## Josuke é um aluno do primeiro ano do ensino médio que mora na cidade de Morioh. Ele logo conhece Jotaro Kujo, que o informa que ele é filho ilegítimo de Joseph Joestar. Depois que seu avô morre, Josuke assume a responsabilidade de proteger sua amada cidade dos malévolos usuários do Stand. Josuke empunha Crazy Diamond, um poderoso Stand com o poder de consertar quase tudo.
                    ''')
    with tab7:
        st.image('giorno2.png')
        st.markdown('''
                    ## Giorno Giovanna (ジョルノ·ジョバァーナJoruno Jobāna) é o protagonista de Vento Aureo e o quinto JoJo da série JoJo's Bizarre Adventure.

## Giorno é o filho ilegítimo de DIO, concebido com o corpo roubado de Jonathan Joestar. Ele é apresentado como Haruno Shiobana (汐華 初流乃). Ele fala de sua intenção de se juntar à poderosa gangue Passione e seu sonho de se tornar um "Gangstar".'''
                    )
    with tab8:
        st.image('jolyne.png')
        st.markdown('''
                    ## Jolyne Cujoh (空条 徐倫Kūjō Jorīn ) é a protagonista da Parte 6 e a sexta JoJo da série JoJo's Bizarre Adventure.

## Jolyne é a única mulher " JoJo " até hoje, e filha de Jotaro Kujo. Inicialmente uma garota comum, Jolyne rapidamente desperta seu Stand baseado em cordas, Stone Free, durante seu tempo na prisão.
                    ''')
    with tab9:
        st.image('johnny.png')
        st.markdown('''
                    ## Johnny Joestar (ジョニィ・ジョースター Joni Jōsutā ) , nascido Jonathan Joestar (ジョナサン・ジョースター Jonasan Jōsutā ) é o protagonista principal de Steel Ball Run e um personagem secundário em JoJolion. Ele é o sétimo JoJo da série JoJo's Bizarre Adventure.

## Um ex -prodígio das corridas de cavalos que se tornou paraplégico, Johnny se junta à corrida SBR para descobrir o segredo por trás das Steel Balls de Gyro Zeppeli, pois são a única coisa capaz de restaurar suas pernas.
                    ''')
    with tab10:
        st.image('gappy.png')
        st.markdown('''
                    ## Josuke Higashikata (東方 定助 Higashikata Jōsuke) é o protagonista principal de JoJolion, o oitavo JoJo da série JoJo's Bizarre Adventure .

## Josuke é um jovem que sofre de amnésia retrógrada, sem nenhuma memória antes de ser descoberto por Yasuho Hirose perto das Paredes Oculares em Morioh Town. Ele se dedica a descobrir sua antiga identidade e aqueles originalmente associados a ele.

## A identidade original de Josuke era a de Josefumi Kujo (空条 仗世文Kūjō Josefumi ) , e tornou-se seu eu atual após a fusão com o homem Yoshikage Kira (吉良 吉影Kira Yoshikage ) . Josuke é um Stand User e mantém sua identidade original Soft & Wet , embora com pequenas mudanças influenciadas por sua outra metade.
                    ''')