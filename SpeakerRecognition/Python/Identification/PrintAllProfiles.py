""" Copyright (c) Microsoft. All rights reserved.
Licensed under the MIT license.

Project Oxford: http://ProjectOxford.ai

Project Oxford SDK Github:
https://github.com/Microsoft/ProjectOxfordSDK-Windows

Copyright (c) Microsoft Corporation
All rights reserved.

MIT License:
Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED ""AS IS"", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import IdentificationServiceHttpClientHelper
import sys

def print_all_profiles(subscription_key):
    """Print all the profiles for the given subscription key.

    Arguments:
    subscription_key -- the subscription key string
    """
    helper = IdentificationServiceHttpClientHelper.IdentificationServiceHttpClientHelper(
        subscription_key)

    profiles = helper.get_all_profiles()

    print('Profile ID, Locale, Enrollment Speech Time, Remaining Enrollment Speech Time,'
          ' Created Date Time, Last Action Date Time, Enrollment Status')
    for i in range(0, len(profiles)):
        print('{0}, {1}, {2}, {3}, {4}, {5}, {6}'.format(
            profiles[i].get_profile_id(),
            profiles[i].get_locale(),
            profiles[i].get_enrollment_speech_time(),
            profiles[i].get_remaining_enrollment_time(),
            profiles[i].get_created_date_time(),
            profiles[i].get_last_action_date_time(),
            profiles[i].get_enrollment_status()))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python PrintAllProfiles.py <subscription_key>')
        print('\t<subscription_key> is the subscription key for the service')
        sys.exit('Error: Incorrect Usage.')

    print_all_profiles(sys.argv[1])
