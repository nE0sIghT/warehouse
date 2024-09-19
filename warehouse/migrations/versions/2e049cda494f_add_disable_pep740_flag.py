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
"""
add DISABLE_PEP740 flag

Revision ID: 2e049cda494f
Revises: f204918656f1
Create Date: 2024-09-05 15:15:58.703955
"""

from alembic import op

revision = "2e049cda494f"
down_revision = "f204918656f1"


def upgrade():
    op.execute(
        """
        INSERT INTO admin_flags(id, description, enabled, notify)
        VALUES (
            'disable-pep740',
            'Disable PEP 740 support.',
            FALSE,
            FALSE
        )
    """
    )


def downgrade():
    op.execute("DELETE FROM admin_flags WHERE id = 'disable-pep740'")