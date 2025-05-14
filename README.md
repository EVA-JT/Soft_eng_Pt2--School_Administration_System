# Soft_eng_Pt2--School_Administration_System
Segunda parte da matéria de engenharia de software.
Projeto original: Humberto Barros

# DESIGN PATTERNS

## Creational
### Factory Method
Implementado em users > final.py . Permite uma criação mais simples de usuários (tutor ou estudante), facilitando o loop e manutenção de dados.

## Structural
### Composite
Implementado em classes > turmas.py . Os dias da semana eram tratados da mesma maneira porem separadamente, portanto foi criado a classe WeekSchedule para um tratamento mais uniforme, ajudando também na manutenção futura.

## Behavioral
### Command
Implementado em classes > timetamble.py. As ações para editar cada horário de cada dia eram feitas a partir de if e elses, portanto foi criado as classes Command, Edit_Time_Command e Editor para cuidar dessas ações, simplificando o processo, facilitando a manutenção e expansão e com uma nova funcionalidade de desfazer edições.
