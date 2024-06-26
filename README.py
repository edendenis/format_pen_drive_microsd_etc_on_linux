#!/usr/bin/env python
# coding: utf-8

# # Como formatar um `Pen Drive`, `MicroSD` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos para formatar um `Pen Drive`, `MicroSD` no `Linux Ubuntu` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands to format a `Pen Drive`, `MicroSD` in `Linux Ubuntu` in `Linux Ubuntu`._
# 

# ## Descrição [2]
# 
# ### `PenDrive`
# 
# Um "PenDrive", também conhecido como unidade flash USB ou memória USB, é um dispositivo de armazenamento portátil que utiliza memória flash para armazenar dados. Ele é amplamente utilizado para transferir, armazenar e transportar dados de forma rápida e conveniente entre diferentes dispositivos, como computadores, laptops, consoles de videogame e sistemas de áudio e vídeo. Os Pendrives são compactos, duráveis e oferecem capacidades de armazenamento que variam de alguns megabytes a várias centenas de gigabytes, permitindo armazenar uma ampla variedade de arquivos, incluindo documentos, fotos, vídeos, músicas e programas. Eles se conectam a dispositivos host por meio de uma porta USB e geralmente são plug-and-play, o que significa que podem ser facilmente conectados e utilizados sem a necessidade de instalação de drivers adicionais. Os Pendrives tornaram-se uma parte essencial da vida cotidiana moderna, sendo utilizados tanto para fins pessoais quanto profissionais, devido à sua praticidade, portabilidade e capacidade de armazenamento.
# 
# ### `MicroSD`
# 
# Um cartão MicroSD é um tipo de cartão de memória flash de tamanho reduzido, projetado para armazenamento de dados em dispositivos eletrônicos compactos, como smartphones, tablets, câmeras digitais e consoles de jogos portáteis. Ele oferece uma forma conveniente de expandir a capacidade de armazenamento desses dispositivos, permitindo que os usuários armazenem uma variedade de conteúdos, incluindo fotos, vídeos, músicas, aplicativos e documentos. Os cartões MicroSD são compactos e leves, tornando-os ideais para uso em dispositivos móveis onde o espaço é limitado. Eles são compatíveis com uma ampla gama de dispositivos e podem ser facilmente inseridos em slots de cartão MicroSD. Com capacidades de armazenamento que variam de alguns gigabytes a vários terabytes, os cartões MicroSD oferecem flexibilidade para usuários que precisam de espaço adicional para seus dados em dispositivos portáteis.
# 
# ### `lsblk`
# 
# O comando "lsblk" é uma ferramenta de linha de comando disponível em sistemas Linux que é usada para listar informações sobre dispositivos de bloco, como discos rígidos (HDDs), unidades de estado sólido (SSDs) e dispositivos de armazenamento USB. Ele exibe uma visão hierárquica dos dispositivos de bloco e suas respectivas partições, incluindo detalhes como o nome do dispositivo, o tipo de disco, o tamanho, o modelo e o ponto de montagem, se aplicável. O "lsblk" é útil para identificar e visualizar a estrutura de armazenamento de um sistema, ajudando os usuários a entender quais dispositivos estão conectados e como estão organizados. Ele é frequentemente usado por administradores de sistema, técnicos de suporte e usuários avançados para gerenciar e diagnosticar dispositivos de armazenamento em sistemas Linux.
# 

# ## 1. Como formatar um `Pen Drive`, `MicroSD` no `Linux Ubuntu` [1][3]
# 
# Para formatar um `pendrive` pelo `Terminal Emulator` do `Linux Ubuntu`, você seguirá alguns passos básicos. Primeiramente, é importante entender que esse processo irá apagar todos os dados no pendrive, então certifique-se de ter feito backup de qualquer informação importante.
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`    

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes APT. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo APT e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.5 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.6 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
# 
#     2.7 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.8 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

# ### 1.1 Identificando o Pendrive com `lsblk`
# 
# O comando lsblk lista todos os dispositivos de bloco disponíveis no sistema, incluindo discos rígidos, pendrives, etc. Para identificar seu pendrive:
# 
# 1. Insira o pendrive no computador.
# 
# 2. Abra o `Terminal Emulator`.
# 
# 3. Digite o comando `lsblk` e pressione `Enter`.
# 
#     Você verá uma lista de dispositivos. Procure por um dispositivo que corresponda ao tamanho do seu pendrive e que não esteja montado em nenhum diretório conhecido do sistema (como /, /home, etc.). Geralmente, pendrives são listados como sdX, onde X é uma letra que identifica unicamente o dispositivo (por exemplo, sdb, sdc).
# 

# ### 1.2 Formatando o Pendrive
# 
# Após identificar o pendrive, você pode formatá-lo. Este exemplo usará o sistema de arquivos FAT32, que é amplamente compatível com a maioria dos sistemas operacionais, mas você pode escolher outro sistema de arquivos conforme sua necessidade (como NTFS, exFAT, ou ext4).
# 
# **Atenção:** Substitua `sdX` pelo identificador correto do seu pendrive. **Tenha muito cuidado** para escolher o dispositivo correto, pois a seleção do dispositivo errado pode resultar na perda de dados de outros drives.
# 
# 1. Desmonte o pendrive se ele estiver montado. Substitua `sdX1` pela partição correta do seu pendrive: `umount /dev/sdX1`
# 
# 2. Formate o pendrive. Para formatar como FAT32, use: `sudo mkfs.vfat -F 32 /dev/sdX1`
# 
#     Se preferir outro sistema de arquivos, substitua `mkfs.vfat` pelo comando correspondente ao sistema de arquivos desejado, como `mkfs.ntfs` para NTFS ou `mkfs.ext4` para ext4.
# 

# ### 1.3 Verificação
# 
# Após a formatação, você pode reconectar o pendrive e usar o `lsblk` novamente para verificar se o pendrive está presente e sem pontos de montagem, indicando que está pronto para uso.
# 
# Lembre-se, este processo irá remover todos os dados do seu pendrive, então proceda com cautela e certifique-se de ter selecionado o dispositivo correto antes de formatar.

# ### 3. Código completo para configurar/instalar
# 
# Para configurar/instalar/usar uma mensagem pelo `lightdm` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     **NÂO** há.
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Formatar Pendrive, MicroSD etc. Pelo Terminal:*** https://chat.openai.com/c/25ab2823-b6f8-4193-8f77-fc378350dc55 (texto adaptado). ChatGPT. Acessado em: 08/02/2024 18:26.
# 
# [2] OPENAI. ***Vs code: editor popular:*** https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42 (texto adaptado). ChatGPT. Acessado em: 08/02/2024 18:26.
# 
