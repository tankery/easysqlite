{

    'targets': [
        {
            'target_name': 'easysqlite',
            'type': '<(component)',

            'include_dirs':[
                'easySQLite',
            ],

            'sources': [
                '<!@(ls easySQLite/*.cpp)',
                'easySQLite/sqlite3.c',
            ],

            'direct_dependent_settings': {
                'include_dirs':[
                    'easySQLite',
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
                    'xcode_settings': {
                        'SDKROOT': 'iphoneos',
                    },
                }],
            ],   # conditions

        },
    ],

    'target_defaults': {
        # Things get confused if multiple targets in the same .gyp file don't have the same configuration
        # names, so define them all here.  (this problem doesn't appear to exist across .gyp files,
        # and it doesn't work to define configurations in globals.gypi).
        'default_configuration': 'Debug',
        'configurations': {
            'Debug': {
            },
            'Release': {
            },
        },

        'conditions': [
            ['OS=="android"', {
                'defines': [
                    'ANDROID',
                ],
            }],
            ['OS=="ios"', {
                'xcode_settings': {
                    'TARGETED_DEVICE_FAMILY': '1,2',
                    'CODE_SIGN_IDENTITY': 'iPhone Developer',
                    'IPHONEOS_DEPLOYMENT_TARGET': '7.1',
                },
            }], # OS=="ios"
        ],   # conditions
    },

}
