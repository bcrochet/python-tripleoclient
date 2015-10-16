#   Copyright 2015 Red Hat, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License"); you may
#   not use this file except in compliance with the License. You may obtain
#   a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.
#


import logging
import os

from cliff import command

from tripleo_common.image.build import ImageBuildManager


class BuildImage(command.Command):
    """Build disk images from YAML definitions"""

    log = logging.getLogger(__name__ + ".DeployOvercloud")

    def get_parser(self, prog_name):
        parser = super(BuildImage, self).get_parser(prog_name)

        parser.add_argument('--config-file',
                            dest='config_files',
                            metavar='CONFIG_FILE',
                            action='append',
                            help="""Path to a configuration file""",
                            default=['disk_images.yaml'])
        parser.add_argument('--output-directory',
                            metavar='DIRECTORY',
                            help="""Output directory for images"""
                                 """Defaults to '.'""",
                            default='.')
        parser.add_argument('--skip',
                            action='store_true',
                            help="""Skip build if cached image exists""",
                            default=False)
        parser.add_argument('--verbose',
                            dest="verbose",
                            action='store_true',
                            help="Print verbose output",
                            required=False)

        return parser

    def take_action(self, parsed_args):
        self.log.debug("take_action(%s)" % parsed_args)

        build_manager = ImageBuildManager(
            parsed_args.config_files,
            output_directory=parsed_args.output_directory,
            node_dist=os.environ.get('NODE_DIST', None),
            skip=parsed_args.skip,
            verbose=parsed_args.skip,
            debug=parsed_args.debug)
        build_manager.build()
