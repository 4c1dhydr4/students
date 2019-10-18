from django.shortcuts import render

def index(request):
	context = {'message': 'Hola Gilipuertas'}
	return render(request, 'students/index.html', context)

def myProfile(request):
	context = {
		'name': 'Luis Augusto Quiroz Burga',
		'photo':'/static/images/admin.png',
		'grade':'5° de Secundaria',
		'code': 'C0002435',
		'dni': '70197949',
		'email': 'luis.quiroz@syncstudent.com',
		'bornDate': '4 de abil de 1993',
		'direction':'Av. La Merced 1015 Block G Dpto 504',
		'phone': '(01) 2556868',
		'cellphone': '+51 980655030',
		'firstDate': '30 de Enero del 2016',
		'global_average': 16.56,
		'actual_average': 17.34,
		'order_of_merit': '02/23',
		'global_order_of_merit': '05/480',
	}
	return render(request, 'students/student_profile.html', context)

def myNotes(request):
	context = {
		'courses': [
			{
				'name': 'Ciencias Sociales',
				'notas': [
							{'period': 'Primer Trimestre' ,'T1': 13,'T2': 14,'T3': 15,'T4': 17,'EP': 14,'EF': 9, 'average': 18},
							{'period': 'Segundo Trimestre' ,'T1': 11,'T2': 15,'T3': 15,'T4': 10,'EP': 10,'EF': 12, 'average': 16},
							{'period': 'Segundo Trimestre' ,'T1': 15,'T2': 17,'T3': 19,'T4': 11,'EP': 11,'EF': 11, 'average': 14},
						],
			},
			{
				'name': 'Matemática Aplicada',
				'notas': [
							{'period': 'Primer Trimestre' ,'T1': 16,'T2': 12,'T3': 13,'T4': 12,'EP': 12,'EF': 6, 'average': 12},
							{'period': 'Segundo Trimestre' ,'T1': 13,'T2': 13,'T3': 14,'T4': 18,'EP': 12,'EF': 17, 'average': 16},
							{'period': 'Segundo Trimestre' ,'T1': 16,'T2': 15,'T3': 19,'T4': 13,'EP': 12,'EF': 18, 'average': 16},
						],
			},
			{
				'name': 'Lengua y Literatura',
				'notas': [
							{'period': 'Primer Trimestre' ,'T1': 13,'T2': 14,'T3': 9,'T4': 12,'EP': 12,'EF': 6, 'average': 13},
							{'period': 'Segundo Trimestre' ,'T1': 11,'T2': 15,'T3': 8,'T4': 18,'EP': 12,'EF': 17, 'average': 11},
							{'period': 'Segundo Trimestre' ,'T1': 10,'T2': 13,'T3': 9,'T4': 13,'EP': 12,'EF': 18, 'average': 11},
						],
			},
			{
				'name': 'Ciencia, Tecnología y Ambiente',
				'notas': [
							{'period': 'Primer Trimestre' ,'T1': 10,'T2': 16,'T3': 10,'T4': 12,'EP': 12,'EF': 6, 'average': 10},
							{'period': 'Segundo Trimestre' ,'T1': 16,'T2': 12,'T3': 13,'T4': 12,'EP': 12,'EF': 6, 'average': 10},
							{'period': 'Segundo Trimestre' ,'T1': 15,'T2': 17,'T3': 11,'T4': 13,'EP': 12,'EF': 18, 'average': 15},
						],
			},
			{
				'name': 'Talleres',
				'notas': [
							{'period': 'Primer Trimestre' ,'T1': 14,'T2': 16,'T3': 17,'T4': 12,'EP': 12,'EF': 6, 'average': 11},
							{'period': 'Segundo Trimestre' ,'T1': 16,'T2': 11,'T3': 8,'T4': 18,'EP': 12,'EF': 17, 'average': 16},
							{'period': 'Segundo Trimestre' ,'T1': 11,'T2': 15,'T3': 15,'T4': 10,'EP': 10,'EF': 12, 'average': 16},
						],
			}
		]
	}
	return render(request, 'students/student_notes.html', context)

def myCourses(request):
	context = {
		'courses': [
			{
				'id': 1,
				'name': 'Ciencias Sociales',
				'description': 'Rama del saber humano constituida por el conjunto de conocimientos objetivos y verificables sobre una materia determinada que son obtenidos mediante la observación y la experimentación, la explicación de sus principios y causas y la formulación y verificación de hipótesis y se caracteriza, además, por la utilización de una metodología adecuada para el objeto de estudio y la sistematización de los conocimientos.',
				'teachers': ['Luis Quiroz Burga', 'Juan Carlos Burga'],
				'image_url': '/static/images/courses/cs.png',
				'messagesN': '03',
				'tasksN': '02',
				'activityN': '02',
				'messages': ['¡Tarea para 29/10 Disponible!', 'Traer colores para la clase del 15/10', 'Leer páginas 25-30'],
				'tasks': ['Entrega Laboratorio Semana 19', 'Entrea de Investigación - Venezuela en el 2018',],
			},
			{
				'id': 2,
				'name': 'Matemáticas Aplicadas',
				'description': 'La enorme utilidad de las matemáticas en las ciencias naturales es algo que roza lo misterioso, y no hay explicación para ello. No es en absoluto natural que existan “leyes de la naturaleza”, y mucho menos que el hombre sea capaz de descubrirlas. El milagro de lo apropiado que resulta el lenguaje de las matemáticas para la formulación de las leyes de la física es un regalo maravilloso que no comprendemos ni nos merecemos.',
				'teachers': ['Alan Turing',],
				'image_url': '/static/images/courses/math.jpg',
				'messagesN': '04',
				'tasksN': '00',
				'activityN': '00',
				'messages': ['¡Tarea para 29/10 Disponible!',],
				'tasks': [],
			},
			{
				'id': 3,
				'name': 'Lengua y Literatura',
				'description': 'Nuestro egresado se distingue por dominar contenidos relacionados con todos los niveles de lenguaje: fónico, morfosintáctico y léxico-semántico. Además, posee conocimientos de latín que le permiten enriquecer el conocimiento de la lengua española como lengua románica. En lo que se respecta a literatura, adquiere un conjunto de contenidos de literatura universal, española, hispanoamericana y peruana.',
				'teachers': ['Alberto Vargas Llosa',],
				'image_url': '/static/images/courses/ll.jpg',
				'messagesN': '02',
				'tasksN': '04',
				'activityN': '04',
				'messages': ['Traer colores para la clase del 15/10',],
				'tasks': ['Entrega Laboratorio Semana 19', 'Entrea de Investigación: Venezuela en el 2018',],
			},
			{
				'id': 4,
				'name': 'Psicología',
				'description': 'Ciencia que estudia los procesos mentales, las sensaciones, las percepciones y el comportamiento del ser humano, en relación con el medio ambiente físico y social que lo rodea.',
				'teachers': ['Dead Pool',],
				'image_url': '/static/images/courses/ps.jpg',
				'messagesN': '00',
				'tasksN': '01',
				'activityN': '02',
				'messages': ['Leer páginas 25-30',],
				'tasks': ['Entrega Laboratorio Semana 19', 'Entrea de Investigación: Venezuela en el 2018',],
			},
			{
				'id': 5,
				'name': 'Talleres',
				'description': 'Ciencia que estudia los procesos mentales, las sensaciones, las percepciones y el comportamiento del ser humano, en relación con el medio ambiente físico y social que lo rodea.',
				'teachers': ['Freddy Vega',],
				'image_url': '/static/images/courses/t.jpeg',
				'messagesN': '04',
				'tasksN': '02',
				'activityN': '01',
				'messages': ['¡Tarea para 29/10 Disponible!', 'Traer colores para la clase del 15/10', 'Leer páginas 25-30'],
				'tasks': ['Entrega Laboratorio Semana 19', 'Entrea de Investigación: Venezuela en el 2018',],
			},
			{
				'id': 6,
				'name': 'Ciencia, Tecnología y Ambiente',
				'description': 'Es el conocimiento sistematizado, elaborado mediante observaciones, razonamientos y pruebas metódicamente organizadas.',
				'teachers': ['Hannibal Lecter',],
				'image_url': '/static/images/courses/cta.jpg',
				'messagesN': '04',
				'tasksN': '00',
				'activityN': '01',
				'messages': ['¡Tarea para 29/10 Disponible!', 'Traer colores para la clase del 15/10', 'Leer páginas 25-30'],
				'tasks': ['Entrega Laboratorio Semana 19', 'Entrea de Investigación: Venezuela en el 2018',],
			},
		]
	}
	return render(request, 'students/student_courses.html', context)
