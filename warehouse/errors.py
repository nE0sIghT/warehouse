# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pyramid.httpexceptions import HTTPForbidden, HTTPUnauthorized
from pyramid.security import Denied


class BasicAuthFailedPassword(HTTPForbidden):
    pass


class BasicAuthBreachedPassword(HTTPUnauthorized):
    pass


class BasicAuthTwoFactorEnabled(HTTPUnauthorized):
    pass


class WarehouseDenied(Denied):
    def __new__(cls, s, *args, reason=None, **kwargs):
        inner = super().__new__(cls, s, *args, **kwargs)
        inner.reason = reason
        return inner
