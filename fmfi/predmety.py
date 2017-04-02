ana, pdr, alg, ine = 'ana', 'pdr', 'alg', 'ine'

predmety_bak = [
	('ma1', 	ana, "Matematická analýza (1)"),
	('ma2', 	ana, "Matematická analýza (2)"),
	('ma3', 	ana, "Matematická analýza (3)"),
	('ma4',		ana, "Matematická analýza (4)"),

	('dm1', 	alg, "Diskrétna matematika (1)"),
	('alg1',	alg, "Algebra (1)"),
	('alg2',	alg, "Algebra (2)"),
	('topo', 	alg, "Topológia"),
	('lag1', 	alg, "Lineárna Algebra a geometria (1) (MAT)"),
	('lag2', 	alg, "Lineárna Algebra a geometria (2) (MAT)"),
	('aag1f', 	alg, "Algebra a geometria (1) (FYZ)"),
	('aag2f', 	alg, "Algebra a geometria (2) (FYZ)"),
	('log1', 	alg, "Teória množín a matematická logika (1)"),
	('tc1', 	alg, "Teória čísel (1)"),
	('odr1', 	pdr, "Obyčajné diferenciálne rovnice (1)"),
	('odr2', 	pdr, "Obyčajné diferenciálne rovnice (2)"),
	('komplex1', ana, "Komplexná analýza (1)"),

	('kmrpdr', 	pdr, "Klasické metódy riešenia parciálnych diferenciálnych rovníc"),
	('mint', 	ana, "Teória miery a integrálu"),
	('fa1', 	ana, "Funkcionálna analýza (1)"),

	('nn', 		ine, "Neurónové siete"),
	('krypto1', ine, "Kryptológia (1)"),

]

predmety_mag = [
	('anava', 	ana, "Analýza na varietách"),
	('dynsys', 	ana, "Dynamické systémy"),
	('nfa', 	ana, "Nelineárna funkcionálna analýza"),

	('pdr1', 	pdr, "Parciálne diferenciálne rovnice (1)"),
	('pdr2', 	pdr, "Parciálne diferenciálne rovnice (2)"),
	('itsf', 	pdr, "Integrálne transformácie a špeciálne funkcie"),

	('vp', 		ana, "Variačný počet"),
	('faq', 	ana, "Funkcionálna analýza (mMAT)"),


	('pocalg', 	alg, "Počítačová algebra"),
	('vstop', 	alg, "Všeobecná topológia"),
	('diftop', 	alg, "Diferenciálna topológia"),
	('algtop', 	alg, "Algebraická topológia"),
]

predmety = predmety_bak + predmety_mag

predmet_to_studium = {abbrev: predmety_bak for abbrev, _, _ in predmety_bak}
predmet_to_studium.update(
	{abbrev: predmety_mag for abbrev, _, _ in predmety_mag}
)
