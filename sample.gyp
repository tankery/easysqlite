{

    'targets': [
        {
            'target_name': 'sample',
            'type': 'executable',

            'dependencies': [
                'easysqlite.gyp:easysqlite',
            ],

            'sources': [
                './sample.cpp'
            ]
        }
    ],

}