# -*- coding: utf-8 -*-

# EFILTER Forensic Query Language
#
# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""EFILTER abstract type system."""

from efilter import dispatch
from efilter import protocol

from efilter.protocols import counted

# Declarations:
# pylint: disable=unused-argument


@dispatch.multimethod
def select(associative, key):
    raise NotImplementedError()


@dispatch.multimethod
def resolve(associative, key):
    raise NotImplementedError()


class IAssociative(protocol.Protocol):
    _protocol_functions = (select, resolve)


IAssociative.implement(for_type=dict,
                       implementations={
                           select: lambda d, key: d.get(key),
                           resolve: lambda d, key: d.get(key)})

IAssociative.implement(for_type=counted.ICounted,
                       implementations={
                           select: lambda c, idx: c[idx],
                           resolve: lambda c, idx: c[idx]})