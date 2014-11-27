{

    'targets': [
        {
            'target_name': 'UnitTest++',
            'type': '<(component)',

            'include_dirs':[
                'src',
            ],

            'sources': [
                'src/AssertException.cpp',
                'src/Test.cpp',
                'src/Checks.cpp',
                'src/TestRunner.cpp',
                'src/TestResults.cpp',
                'src/TestReporter.cpp',
                'src/TestReporterStdout.cpp',
                'src/ReportAssert.cpp',
                'src/TestList.cpp',
                'src/TimeConstraint.cpp',
                'src/TestDetails.cpp',
                'src/MemoryOutStream.cpp',
                'src/DeferredTestReporter.cpp',
                'src/DeferredTestResult.cpp',
                'src/XmlTestReporter.cpp',
                'src/CurrentTest.cpp',
            ],

            'direct_dependent_settings': {
                'include_dirs':[
                    'src',
                ],
            },

            'conditions': [
                ['OS=="win32"', {
                    'sources': [
                        'src/Win32/TimeHelpers.cpp',
                    ],
                }],
                ['OS!="win32"', {
                    'sources': [
                        'src/Posix/TimeHelpers.cpp',
                        'src/Posix/SignalTranslator.cpp',
                    ],
                }],
            ],   # conditions
        },
    ],

}