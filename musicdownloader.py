import pafy

url = str(input("Url: ")).strip()
video = pafy.new(url)
audiostreams = video.audiostreams
locallucas = 'C:/Users/user/Music/Músicas Lucas'
localmat = 'C:/Users/user/Music/Músicas Matheus'
cont = -1
for i in audiostreams:
    cont += 1
    print(f"{cont}, Qualidade: {i.bitrate}, Extensão: {i.extension}, Tamanho: {i.get_filesize()/1024:}MB")
o = int(input("Digite a opção: "))
print("""Local:
[ 1 ] Músicas do Lucas
[ 2 ] Músicas do Matheus""")
l = int(input("Digite sua escolha: "))
if l == 1:
    print("Baixando...")
    audiostreams[o].download(filepath = locallucas)
    print("Download concluído")
elif l == 2:
    print("Baixando...")
    audiostreams[o].download(filepath = localmat)
    print("Download concluído")
