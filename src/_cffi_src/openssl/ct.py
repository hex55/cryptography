# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.

from __future__ import absolute_import, division, print_function

INCLUDES = """
#if CRYPTOGRAPHY_OPENSSL_110_OR_GREATER && !defined(LIBRESSL_VERSION_NUMBER)
#include <openssl/ct.h>

typedef STACK_OF(SCT) Cryptography_STACK_OF_SCT;
#endif
"""

TYPES = """
static const long Cryptography_HAS_SCT;

typedef enum {
    SCT_VERSION_NOT_SET,
    SCT_VERSION_V1
} sct_version_t;

typedef enum {
    CT_LOG_ENTRY_TYPE_NOT_SET,
    CT_LOG_ENTRY_TYPE_X509,
    CT_LOG_ENTRY_TYPE_PRECERT
} ct_log_entry_type_t;

typedef ... SCT;
typedef ... Cryptography_STACK_OF_SCT;
"""

FUNCTIONS = """
"""

MACROS = """
sct_version_t SCT_get_version(const SCT *);

ct_log_entry_type_t SCT_get_log_entry_type(const SCT *);

size_t SCT_get0_log_id(const SCT *, unsigned char **);

uint64_t SCT_get_timestamp(const SCT *);

int sk_SCT_num(const Cryptography_STACK_OF_SCT *);
SCT *sk_SCT_value(const Cryptography_STACK_OF_SCT *, int);
"""

CUSTOMIZATIONS = """
#if CRYPTOGRAPHY_OPENSSL_110_OR_GREATER && !defined(LIBRESSL_VERSION_NUMBER)
static const long Cryptography_HAS_SCT = 1;
#else
static const long Cryptography_HAS_SCT = 0;

typedef enum {
    SCT_VERSION_NOT_SET,
    SCT_VERSION_V1
} sct_version_t;
typedef enum {
    CT_LOG_ENTRY_TYPE_NOT_SET,
    CT_LOG_ENTRY_TYPE_X509,
    CT_LOG_ENTRY_TYPE_PRECERT
} ct_log_entry_type_t;
typedef void SCT;
typedef void Cryptography_STACK_OF_SCT;

sct_version_t (*SCT_get_version)(const SCT *) = NULL;
ct_log_entry_type_t (*SCT_get_log_entry_type)(const SCT *) = NULL;
size_t (*SCT_get0_log_id)(const SCT *, unsigned char **) = NULL;
uint64_t (*SCT_get_timestamp)(const SCT *) = NULL;

int (*sk_SCT_num)(const Cryptography_STACK_OF_SCT *) = NULL;
SCT *(*sk_SCT_value)(const Cryptography_STACK_OF_SCT *, int) = NULL;
#endif
"""
