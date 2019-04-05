#!/bin/bash
# ==============================================================================
# Copyright 2017 Baidu.com, Inc. All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================


if [[ -d preprocessed ]]; then
    echo "data exist"
    exit 0
else
    # download preprocessed data
    wget -c https://aipedataset.cdn.bcebos.com/dureader/dureader_preprocessed.zip
    # download trained model parameters
    wget -c TBD
    # download vocabularies
    wget -c TBD

    # decompression
    unzip dureader_preprocessed.zip
    unzip saved_model.zip
    unzip vocab.zip
fi
