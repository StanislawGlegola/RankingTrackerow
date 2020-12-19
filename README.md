# RankingTrackerow

Ranking najpopularniejszych track'ów (proces ETL)
Celem zadania jest napisanie aplikacji, która:

wczyta dane z plików zawierających dane dotyczące artystów, ich utworów oraz odsłuchań,
przekształci dane w taki sposób by można było je umieścić w bazie danych (np. SQlite),
wypisze na standardowe wyjście informacje, takie jak: artysta z największą liczbą odsłuchań, 5 najpopularniejszych utworów oraz czas przetwarzania danych.
Źródło danych:

plik unique_tracks.txt - zawiera dane w następującym formacie: identyfikator wykonania<SEP>identyfikator utworu<SEP>nazwa artysty<SEP>tytuł utworu<SEP>czas utworu w sekundach<LF>
plik triplets_sample_20p.txt - zawiera dane w następującym formacie: identyfikator użytkownika<SEP>identyfikator utworu<SEP>datę odsłuchania<LF>
