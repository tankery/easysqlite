{

    'targets': [
        {
            'target_name': 'easysqlite',
            'type': '<(component)',

            'include_dirs':[
                '.',
            ],

            'sources': [
                '<!@(ls easySQLite/*.cpp)',
                'easySQLite/sqlite3.c',
            ],

            'direct_dependent_settings': {
                'include_dirs':[
                    '.',
                ],

                'conditions': [
                    ['OS=="android"', {
                        'defines': [
                            'ESQL_NO_EXCEPTION_HANDLING',
                        ],
                    }],
                    ['OS=="ios"', {
                        'defines': [
                            'ESQL_NO_EXCEPTION_HANDLING',
                        ],
                    }],
                ],   # conditions
            },

            'conditions': [
                ['OS=="android"', {
                    'defines': [
                        'ESQL_NO_EXCEPTION_HANDLING',
                    ],
                }],
                ['OS=="ios"', {
                    'defines': [
                        'ESQL_NO_EXCEPTION_HANDLING',
                    ],
                }],
            ],   # conditions

        },
    ],

    'conditions': [
        ['OS=="linux"', {
            'targets': [
                {
                    'target_name': 'easysqlite_test',
                    'type': 'executable',

                    'sources': [
                        'easySQLite.cpp',
                        '<!@(ls Tests/*.cpp)',
                    ],

                    'dependencies': [
                        'easysqlite',
                        'UnitTest++/UnitTest++.gyp:UnitTest++',
                    ],

                },
            ],
        }],
    ],   # conditions

}
