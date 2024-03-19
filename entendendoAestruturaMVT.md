# Projeto Django

    ## Estrutura de diretório/pastas

    projeto
        - projeto
            - settings.py   -> configuração do sistema
            - urls.py       -> roteamento geral
        - core
            - models.py
            - urls.py
            - views.py
            - template
                - core
                    html e css
        - usuario
            - models.py
            - urls.py       -> roteamento local
            - views.py      -> regras de negócios - CRUD e validações
            - forms.py
            - template
                - usuario
                    - usuario_list.html
                    - usuario_form.html
                    - usuario_delete.html
        - utils             -> Classes e métodos de ajuda