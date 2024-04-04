PREFIXES_QUERY_PART = """\
PREFIX besluittype: <https://data.vlaanderen.be/id/concept/BesluitType/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX mu: <http://mu.semte.ch/vocabularies/core/>
PREFIX task: <http://redpencil.data.gift/vocabularies/tasks/>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX prov: <http://www.w3.org/ns/prov#>
PREFIX nie: <http://www.semanticdesktop.org/ontologies/2007/01/19/nie#>
PREFIX ext: <http://mu.semte.ch/vocabularies/ext/>
PREFIX oslc: <http://open-services.net/ns/core#>
PREFIX cogs: <http://vocab.deri.ie/cogs#>
PREFIX adms: <http://www.w3.org/ns/adms#>
PREFIX nfo: <http://www.semanticdesktop.org/ontologies/2007/03/22/nfo#>
PREFIX dbpedia: <http://dbpedia.org/resource/>
PREFIX besluit: <http://data.vlaanderen.be/ns/besluit#>
PREFIX besluitvor: <https://data.vlaanderen.be/ns/besluitvorming#>
PREFIX generiek: <https://data.vlaanderen.be/ns/generiek#>
PREFIX dossier: <https://data.omgeving.vlaanderen.be/ns/dossier#>
PREFIX org: <http://www.w3.org/ns/org#>
PREFIX eurm8g: <http://data.europa.eu/m8g/>
PREFIX locn: <http://www.w3.org/ns/locn#>
PREFIX eli: <http://data.europa.eu/eli/ontology#>
PREFIX sh: <http://www.w3.org/ns/shacl#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX mandaat: <http://data.vlaanderen.be/ns/mandaat#>
PREFIX harvesting: <http://lblod.data.gift/vocabularies/harvesting/>
PREFIX deltas: <http://redpencil.data.gift/vocabularies/deltas/Error>
PREFIX leidinggevenden: <http://data.lblod.info/vocabularies/leidinggevenden/>
PREFIX vlaanderenconcept: <https://data.vlaanderen.be/id/concept/>
PREFIX lblodbesluit: <http://lblod.data.gift/vocabularies/besluit/>
PREFIX lblodeditor: <http://lblod.data.gift/vocabularies/editor/>
PREFIX vlaanderenmobiliteit: <https://data.vlaanderen.be/ns/mobiliteit#>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfa: <http://www.w3.org/ns/rdfa#>
PREFIX xhv: <http://www.w3.org/1999/xhtml/vocab#>
PREFIX dennis: <https://codifly.be/ns/dennis#>
"""

FISCAL_RESOLUTUON_CLASSES_QUERY_PART="""\
VALUES (?fiscalClass ?fiscalClassLabel) {
  (<https://data.vlaanderen.be/id/concept/BesluitType/4c22ef0a-f808-41dd-9c9f-2aff17fd851f> "Contantbelasting" )
  (<https://data.vlaanderen.be/id/concept/BesluitType/8597e056-b96d-4213-ad4c-37338f2aaf35> "Kohierbelasting" )
  (<https://data.vlaanderen.be/id/concept/BesluitType/b2d0734d-13d0-44b4-9af8-1722933c5288> "Aanvullende belasting" )
  (<https://data.vlaanderen.be/id/concept/BesluitType/efa4ec5a-b006-453f-985f-f986ebae11bc> "Belastingsreglement" )
}
"""

ADMIN_UNIT_CLASSIFICATION_VALUES_QUERY_PART="""\
VALUES (?adminUnitClassification ?adminUnitClassificationLabel) {
  (<http://data.vlaanderen.be/id/concept/BestuurseenheidClassificatieCode/293e5f58-9544-496e-88e0-734a137f6ebc> "Watering")
  (<http://data.vlaanderen.be/id/concept/BestuurseenheidClassificatieCode/36a82ba0-7ff1-4697-a9dd-2e94df73b721> "Autonoom gemeentebedrijf")
  (<http://data.vlaanderen.be/id/concept/BestuurseenheidClassificatieCode/5ab0e9b8a3b2ca7c5e000000> "Provincie")
  (<http://data.vlaanderen.be/id/concept/BestuurseenheidClassificatieCode/5ab0e9b8a3b2ca7c5e000001> "Gemeente")
  (<http://data.vlaanderen.be/id/concept/BestuurseenheidClassificatieCode/5ab0e9b8a3b2ca7c5e000002> "OCMW")
  (<http://data.vlaanderen.be/id/concept/BestuurseenheidClassificatieCode/5ab0e9b8a3b2ca7c5e000003> "District")
  (<http://data.vlaanderen.be/id/concept/BestuurseenheidClassificatieCode/66ec74fd-8cfc-4e16-99c6-350b35012e86> "Bestuur van de eredienst")
  (<http://data.vlaanderen.be/id/concept/BestuurseenheidClassificatieCode/80310756-ce0a-4a1b-9b8e-7c01b6cc7a2d> "Autonoom provinciebedrijf")
  (<http://data.vlaanderen.be/id/concept/BestuurseenheidClassificatieCode/a3922c6d-425b-474f-9a02-ffb71a436bfc> "Politiezone")
  (<http://data.vlaanderen.be/id/concept/BestuurseenheidClassificatieCode/b156b67f-c5f4-4584-9b30-4c090be02fdc> "Projectvereniging")
  (<http://data.vlaanderen.be/id/concept/BestuurseenheidClassificatieCode/cc4e2d67-603b-4784-9b61-e50bac1ec089> "OCMW vereniging")
  (<http://data.vlaanderen.be/id/concept/BestuurseenheidClassificatieCode/cd93f147-3ece-4308-acab-5c5ada3ec63d> "Opdrachthoudende vereniging")
  (<http://data.vlaanderen.be/id/concept/BestuurseenheidClassificatieCode/d01bb1f6-2439-4e33-9c25-1fc295de2e71> "Dienstverlenende vereniging")
  (<http://data.vlaanderen.be/id/concept/BestuurseenheidClassificatieCode/d312c541-a263-4004-bca2-63eb991458c3> "Polders")
  (<http://data.vlaanderen.be/id/concept/BestuurseenheidClassificatieCode/e8294b73-87c9-4fa2-9441-1937350763c9> "Welzijnsvereniging")
  (<http://data.vlaanderen.be/id/concept/BestuurseenheidClassificatieCode/ea446861-2c51-45fa-afd3-4e4a37b71562> "Hulpverleningszone")
  (<http://data.vlaanderen.be/id/concept/BestuurseenheidClassificatieCode/f9cac08a-13c1-49da-9bcb-f650b0604054> "Centraal bestuur van de eredienst")
  (<http://data.vlaanderen.be/id/concept/BestuurseenheidClassificatieCode/d90c511e-f827-488c-84ba-432c8f69561c> "Vlaamse gemeenschapscommissie")
}
"""

GOVERNING_BODY_CLASSIFICATION_VALUES_QUERY_PART="""\
VALUES (?governingBodyClassification ?governingBodyClassificationLabel) {
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/11f0af9e-016c-4e0b-983a-d8bc73804abc> "Adjunct-algemeen directeur")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/ed40469e-3b6f-4f38-99ba-18912ee352b0> "Adjunct-financieel directeur")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/39854196-f214-4688-87a1-d6ad12baa2fa> "Algemeen directeur")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/b52094ff-21a2-4da8-8dbe-f513365d1528> "Algemene vergadering")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/90a9ec83cb93b9369bba7ff29d9ce5ce> "Bestuursraad")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/0dbc70ec-6be9-4997-b8e1-11b6c0542382> "Bevoegd beslissingsorgaan")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/5ab0e9b8a3b2ca7c5e000009> "Bijzonder Comité voor de Sociale Dienst")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/4955bd72cd0e4eb895fdbfab08da0284> "Burgemeester")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/4393389e99127b68e7fc11936ba92e18> "Centraal bestuur")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/0d985699479162198b889f10e4f1a8ce> "Centraal kerkbestuur")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/7148e12a-ae03-4a7b-bb16-7b6269b84175> "College")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/5ab0e9b8a3b2ca7c5e000006> "College van Burgemeester en Schepenen")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/ff20fa3e-806b-4160-b74b-7483fe3a6ecd> "Collegelid")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/b475fa47e17a8a05ae04a9e1fb9c9258> "Comité")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/5ab0e9b8a3b2ca7c5e00000d> "Deputatie")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/5733254e-73ff-4844-8d43-7afb7ec726e8> "Directiecomité")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/9314533e-891f-4d84-a492-0338af104065> "Districtsburgemeester")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/5ab0e9b8a3b2ca7c5e00000b> "Districtscollege")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/5ab0e9b8a3b2ca7c5e00000a> "Districtsraad")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/3e9f22c1-0d35-445b-8a37-494addedf2d8> "Financieel beheerder")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/62644b9c-4514-41dd-a660-4c35257f2b35> "Financieel directeur")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/5ab0e9b8a3b2ca7c5e000005> "Gemeenteraad")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/180a2fba-6ca9-4766-9b94-82006bb9c709> "Gouverneur")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/5ab19107-82d2-4273-a986-3da86fda050d> "Griffier")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/a0701624aefb115b7eda2ff39139c2dd> "Kathedrale kerkraad")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/af811edba97c6ec34874d0830cbb1183> "Kerkfabriekraad")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/04f65457bf125b2dc59fd71917ac3d08> "Kerkraad")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/41caf7e6-b040-4720-9cc2-a96cfffed5b4> "Leidend Ambtenaar")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/1afce932-53c1-46d8-8aab-90dcc331e67d> "Politieraad")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/5ab0e9b8a3b2ca7c5e00000c> "Provincieraad")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/013cc838-173a-4657-b1ae-b00c048df943> "Raad van bestuur")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/17e76b36-64a1-4db1-8927-def3064b4bf1> "Regionaal bestuurscomité")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/5ab0e9b8a3b2ca7c5e000008> "Vast Bureau")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/4c38734d-2cc1-4d33-b792-0bd493ae9fc2> "Voorzitter van de Gemeenteraad")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/e14fe683-e061-44a2-b7c8-e10cab4e6ed9> "Voorzitter van de Raad voor Maatschappelijk Welzijn")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/53c0d8cd-f3a2-411d-bece-4bd83ae2bbc9> "Voorzitter van het Bijzonder Comité voor de Sociale Dienst")
  (<http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/a9e30e31-0cd2-4f4a-9352-545c5d43be83> "Zoneraad")
}
"""

MUNICIPALITY_SUPPLIER_VALUES_QUERY_PART = """\
  VALUES (?municipalityName ?supplier) {
    ("Aalst" "GreenValley")
    ("Aalter" "GreenValley")
    ("Aarschot" "Cipal")
    ("Aartselaar" "Cipal")
    ("Affligem" "Cipal")
    ("Alken" "Remmicom")
    ("Alveringem" "Cipal")
    ("Antwerpen" "GreenValley")
    ("Antwerpen" "toepassing")
    ("Anzegem" "Cipal")
    ("Ardooie" "Cipal")
    ("Arendonk" "GreenValley")
    ("As" "GreenValley")
    ("Asse" "Remmicom")
    ("Assenede" "Cevi")
    ("Avelgem" "Cevi")
    ("Baarle-Hertog" "GN")
    ("Balen" "GreenValley")
    ("Beernem" "Cipal")
    ("Beerse" "GreenValley")
    ("Beersel" "Remmicom")
    ("Begijnendijk" "Remmicom")
    ("Bekkevoort" "Remmicom")
    ("Beringen" "GreenValley")
    ("Berlaar" "GreenValley")
    ("Berlare" "Cevi")
    ("Bertem" "Remmicom")
    ("Bever" "Cipal")
    ("Beveren" "GreenValley")
    ("Bierbeek" "Remmicom")
    ("Bilzen" "Tobania")
    ("Blankenberge" "Cevi")
    ("Bocholt" "GreenValley")
    ("Boechout" "Remmicom")
    ("Bonheiden" "Cipal")
    ("Boom" "Cipal")
    ("Boortmeerbeek" "Remmicom")
    ("Borgloon" "GreenValley")
    ("Bornem" "Cipal")
    ("Borsbeek" "GreenValley")
    ("Boutersem" "Remmicom")
    ("Brakel" "Cipal")
    ("Brasschaat" "Remmicom")
    ("Brecht" "Cipal")
    ("Bredene" "Cevi")
    ("Bree" "Cipal")
    ("Brugge" "GreenValley")
    ("Buggenhout" "Cevi")
    ("Damme" "Cevi")
    ("De" "Cevi")
    ("De" "Cevi")
    ("De" "Cipal")
    ("Deerlijk" "Remmicom")
    ("Deinze" "Cipal")
    ("Denderleeuw" "Cevi")
    ("Dendermonde" "Cevi")
    ("Dentergem" "Cipal")
    ("Dessel" "Combinatie")
    ("Destelbergen" "Combinatie")
    ("Diepenbeek" "GreenValley")
    ("Diest" "GreenValley")
    ("Diksmuide" "Cevi")
    ("Dilbeek" "Combinatie")
    ("Dilsen-Stokkem" "GreenValley")
    ("Drogenbos" "Remmicom")
    ("Duffel" "Combinatie")
    ("Edegem" "GreenValley")
    ("Eeklo" "Tobania")
    ("Erpe-Mere" "Cevi")
    ("Essen" "GN")
    ("Evergem" "Cevi")
    ("Galmaarden" "Cipal")
    ("Gavere" "Cipal")
    ("Geel" "GreenValley")
    ("Geetbets" "Cipal")
    ("Genk" "GreenValley")
    ("Gent" "GreenValley")
    ("Geraardsbergen" "Cipal")
    ("Gingelom" "GreenValley")
    ("Gistel" "Cevi")
    ("Glabbeek" "Cipal")
    ("Gooik" "Cipal")
    ("Grimbergen" "Cipal")
    ("Grobbendonk" "Cipal")
    ("Haacht" "GreenValley")
    ("Haaltert" "Cipal")
    ("Halen" "GreenValley")
    ("Halle" "GreenValley")
    ("Ham" "GreenValley")
    ("Hamme" "Cipal")
    ("Hamont-Achel" "GreenValley")
    ("Harelbeke" "Cevi")
    ("Hasselt" "GreenValley")
    ("Hechtel-Eksel" "GreenValley")
    ("Heers" "GreenValley")
    ("Heist-op-den-Berg" "GreenValley")
    ("Hemiksem" "Remmicom")
    ("Herent" "Cipal")
    ("Herentals" "GreenValley")
    ("Herenthout" "Cipal")
    ("Herk-de-Stad" "Cipal")
    ("Herne" "Cipal")
    ("Herselt" "Remmicom")
    ("Herstappe" "GN")
    ("Herzele" "Cevi")
    ("Heusden-Zolder" "Remmicom")
    ("Heuvelland" "Cevi")
    ("Hoegaarden" "Cipal")
    ("Hoeilaart" "Remmicom")
    ("Hoeselt" "Remmicom")
    ("Holsbeek" "Remmicom")
    ("Hooglede" "Cipal")
    ("Hoogstraten" "Remmicom")
    ("Horebeke" "Cevi")
    ("Houthalen-Helchteren" "Remmicom")
    ("Houthulst" "Cevi")
    ("Hove" "Remmicom")
    ("Huldenberg" "Cipal")
    ("Hulshout" "Remmicom")
    ("Ichtegem" "Cevi")
    ("Ieper" "Cipal")
    ("Ingelmunster" "Cevi")
    ("Izegem" "Cevi")
    ("Jabbeke" "Cevi")
    ("Kalmthout" "Lbabs")
    ("Kampenhout" "Cipal")
    ("Kapellen" "Remmicom")
    ("Kapelle-op-den-Bos" "Cipal")
    ("Kaprijke" "Cevi")
    ("Kasterlee" "Remmicom")
    ("Keerbergen" "Remmicom")
    ("Kinrooi" "Cipal")
    ("Kluisbergen" "Cevi")
    ("Knokke-Heist" "Cevi")
    ("Koekelare" "Cipal")
    ("Koksijde" "Cipal")
    ("Kontich" "Cipal")
    ("Kortemark" "Cipal")
    ("Kortenaken" "Cevi")
    ("Kortenberg" "Combinatie")
    ("Kortessem" "GreenValley")
    ("Kortrijk" "GreenValley")
    ("Kraainem" "Remmicom")
    ("Kruibeke" "Cevi")
    ("Kruisem" "Cipal")
    ("Kuurne" "Cipal")
    ("Laakdal" "Tobania")
    ("Laarne" "Cevi")
    ("Lanaken" "Combinatie")
    ("Landen" "Cevi")
    ("Langemark-Poelkapelle" "GreenValley")
    ("Lebbeke" "Cevi")
    ("Lede" "Cevi")
    ("Ledegem" "Cevi")
    ("Lendelede" "Cevi")
    ("Lennik" "Cipal")
    ("Leopoldsburg" "GreenValley")
    ("Leuven" "GreenValley")
    ("Lichtervelde" "Cipal")
    ("Liedekerke" "Cevi")
    ("Lier" "Remmicom")
    ("Lierde" "Cevi")
    ("Lievegem" "Cipal")
    ("Lille" "Combinatie")
    ("Limburg" "Combinatie")
    ("Linkebeek" "GN")
    ("Lint" "Cipal")
    ("Linter" "Cipal")
    ("Lochristi" "Cevi")
    ("Lokeren" "GreenValley")
    ("Lommel" "GreenValley")
    ("Londerzeel" "Cipal")
    ("Lo-Reninge" "Cevi")
    ("Lubbeek" "Cipal")
    ("Lummen" "GreenValley")
    ("Maarkedal" "Cevi")
    ("Maaseik" "GreenValley")
    ("Maasmechelen" "GreenValley")
    ("Machelen" "Cipal")
    ("Maldegem" "Remmicom")
    ("Malle" "Remmicom")
    ("Mechelen" "Cevi")
    ("Meerhout" "Remmicom")
    ("Meise" "Remmicom")
    ("Melle" "Cevi")
    ("Menen" "Cipal")
    ("Merchtem" "Cipal")
    ("Merelbeke" "Cevi")
    ("Merksplas" "Cipal")
    ("Mesen" "GN")
    ("Meulebeke" "Cevi")
    ("Middelkerke" "Cevi")
    ("Moerbeke" "Cipal")
    ("Mol" "Remmicom")
    ("Moorslede" "Cipal")
    ("Mortsel" "GreenValley")
    ("Nazareth" "Cipal")
    ("Niel" "Cevi")
    ("Nieuwerkerken" "GreenValley")
    ("Nieuwpoort" "Cevi")
    ("Nijlen" "GreenValley")
    ("Ninove" "Cevi")
    ("Olen" "Remmicom")
    ("Oostende" "GreenValley")
    ("Oosterzele" "Cevi")
    ("Oostkamp" "Combinatie")
    ("Oostrozebeke" "Cipal")
    ("Oost-Vlaanderen" "GreenValley")
    ("Opwijk" "GreenValley")
    ("Oudenaarde" "Cevi")
    ("Oudenburg" "Cipal")
    ("Oud-Heverlee" "Cipal")
    ("Oudsbergen" "Tobania")
    ("Oud-Turnhout" "GreenValley")
    ("Overijse" "Cipal")
    ("Peer" "GreenValley")
    ("Pelt" "Tobania")
    ("Pepingen" "Cipal")
    ("Pittem" "Cipal")
    ("Poperinge" "Cevi")
    ("Putte" "Combinatie")
    ("Puurs-Sint-Amands" "Cipal")
    ("Ranst" "Remmicom")
    ("Ravels" "GreenValley")
    ("Retie" "Cipal")
    ("Riemst" "Remmicom")
    ("Rijkevorsel" "Cipal")
    ("Roeselare" "GreenValley")
    ("Ronse" "Cevi")
    ("Roosdaal" "Remmicom")
    ("Rotselaar" "Remmicom")
    ("Ruiselede" "Cipal")
    ("Rumst" "GreenValley")
    ("Schelle" "Remmicom")
    ("Scherpenheuvel-Zichem" "Cevi")
    ("Schilde" "Remmicom")
    ("Schoten" "Remmicom")
    ("Sint-Genesius-Rode" "Cipal")
    ("Sint-Gillis-Waas" "Cevi")
    ("Sint-Katelijne-Waver" "GreenValley")
    ("Sint-Laureins" "Cipal")
    ("Sint-Lievens-Houtem" "Cevi")
    ("Sint-Martens-Latem" "Cipal")
    ("Sint-Niklaas" "GreenValley")
    ("Sint-Pieters-Leeuw" "GreenValley")
    ("Sint-Truiden" "GreenValley")
    ("Spiere-Helkijn" "Cipal")
    ("Stabroek" "Tobania")
    ("Staden" "Cipal")
    ("Steenokkerzeel" "Cipal")
    ("Stekene" "Cevi")
    ("Temse" "Cevi")
    ("Ternat" "Cipal")
    ("Tervuren" "Cipal")
    ("Tessenderlo" "GreenValley")
    ("Tielt" "Cipal")
    ("Tielt-Winge" "Remmicom")
    ("Tienen" "Cipal")
    ("Tongeren" "GreenValley")
    ("Torhout" "Cevi")
    ("Tremelo" "Remmicom")
    ("Turnhout" "GreenValley")
    ("Veurne" "Cevi")
    ("Vilvoorde" "GreenValley")
    ("Vlaams-Brabant" "GN")
    ("Vleteren" "Cevi")
    ("Voeren" "Cevi")
    ("Vorselaar" "GreenValley")
    ("Vosselaar" "GreenValley")
    ("Waasmunster" "Cipal")
    ("Wachtebeke" "Cipal")
    ("Waregem" "Cevi")
    ("Wellen" "Remmicom")
    ("Wemmel" "Remmicom")
    ("Wervik" "Cevi")
    ("Westerlo" "GreenValley")
    ("West-Vlaanderen" "Cevi")
    ("Wetteren" "Cevi")
    ("Wevelgem" "Cipal")
    ("Wezembeek-Oppem" "Remmicom")
    ("Wichelen" "Cevi")
    ("Wielsbeke" "Cevi")
    ("Wijnegem" "GreenValley")
    ("Willebroek" "Combinatie")
    ("Wingene" "Cipal")
    ("Wommelgem" "Remmicom")
    ("Wortegem-Petegem" "Cevi")
    ("Wuustwezel" "GreenValley")
    ("Zandhoven" "Cipal")
    ("Zaventem" "Cipal")
    ("Zedelgem" "Lbabs")
    ("Zele" "Cevi")
    ("Zelzate" "Cevi")
    ("Zemst" "Cipal")
    ("Zoersel" "Combinatie")
    ("Zonhoven" "GreenValley")
    ("Zonnebeke" "Cevi")
    ("Zottegem" "Cevi")
    ("Zoutleeuw" "Cipal")
    ("Zuienkerke" "Cevi")
    ("Zulte" "Cipal")
    ("Zutendaal" "GreenValley")
    ("Zwalm" "Cipal")
    ("Zwevegem" "Cevi")
    ("Zwijndrecht" "GreenValley")
  }
"""

LIST_GOVERNING_BODY_URIS = [
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/013cc838-173a-4657-b1ae-b00c048df943", "Raad van bestuur"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/0dbc70ec-6be9-4997-b8e1-11b6c0542382", "Bevoegd beslissingsorgaan"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/11f0af9e-016c-4e0b-983a-d8bc73804abc", "Adjunct-algemeen directeur"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/17e76b36-64a1-4db1-8927-def3064b4bf1", "Regionaal bestuurscomité"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/180a2fba-6ca9-4766-9b94-82006bb9c709", "Gouverneur"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/1afce932-53c1-46d8-8aab-90dcc331e67d", "Politieraad"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/39854196-f214-4688-87a1-d6ad12baa2fa", "Algemeen directeur"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/3e9f22c1-0d35-445b-8a37-494addedf2d8", "Financieel beheerder"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/41caf7e6-b040-4720-9cc2-a96cfffed5b4", "Leidend Ambtenaar"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/4955bd72cd0e4eb895fdbfab08da0284", "Burgemeester"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/4c38734d-2cc1-4d33-b792-0bd493ae9fc2", "Voorzitter van de Gemeenteraad"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/53c0d8cd-f3a2-411d-bece-4bd83ae2bbc9", "Voorzitter van het Bijzonder Comité voor de Sociale Dienst"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/5733254e-73ff-4844-8d43-7afb7ec726e8", "Directiecomité"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/5ab0e9b8a3b2ca7c5e000005", "Gemeenteraad"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/5ab0e9b8a3b2ca7c5e000006", "College van Burgemeester en Schepenen"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/5ab0e9b8a3b2ca7c5e000007", "Raad voor Maatschappelijk Welzijn"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/5ab0e9b8a3b2ca7c5e000008", "Vast Bureau"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/5ab0e9b8a3b2ca7c5e000009", "Bijzonder Comité voor de Sociale Dienst"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/5ab0e9b8a3b2ca7c5e00000a", "Districtsraad"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/5ab0e9b8a3b2ca7c5e00000b", "Districtscollege"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/5ab0e9b8a3b2ca7c5e00000c", "Provincieraad"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/5ab0e9b8a3b2ca7c5e00000d", "Deputatie"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/5ab19107-82d2-4273-a986-3da86fda050d", "Griffier"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/62644b9c-4514-41dd-a660-4c35257f2b35", "Financieel directeur"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/9314533e-891f-4d84-a492-0338af104065", "Districtsburgemeester"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/a9e30e31-0cd2-4f4a-9352-545c5d43be83", "Zoneraad"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/b52094ff-21a2-4da8-8dbe-f513365d1528", "Algemene vergadering"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/e14fe683-e061-44a2-b7c8-e10cab4e6ed9", "Voorzitter van de Raad voor Maatschappelijk Welzijn"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/ed40469e-3b6f-4f38-99ba-18912ee352b0", "Adjunct-financieel directeur"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/04f65457bf125b2dc59fd71917ac3d08", "Kerkraad"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/0d985699479162198b889f10e4f1a8ce", "Centraal kerkbestuur"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/4393389e99127b68e7fc11936ba92e18", "Centraal bestuur"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/7148e12a-ae03-4a7b-bb16-7b6269b84175", "College"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/90a9ec83cb93b9369bba7ff29d9ce5ce", "Bestuursraad"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/a0701624aefb115b7eda2ff39139c2dd", "Kathedrale kerkraad"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/af811edba97c6ec34874d0830cbb1183", "Kerkfabriekraad"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/b475fa47e17a8a05ae04a9e1fb9c9258", "Comité"),
  ("http://data.vlaanderen.be/id/concept/BestuursorgaanClassificatieCode/ff20fa3e-806b-4160-b74b-7483fe3a6ecd", "Collegelid"),
]
