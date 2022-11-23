class Tokenizer:
    def tokenize(self, source):
        source = list(source)
        tokens = self.token()
        dumper = ""
        tokenized = []
        t_suggest = {}
        t_space_standby_token_name = ""
        t_space_standby = "";
        for source_letter in source:
            dumper += source_letter
            recognize_separator = tokens["HNT_READABILITY_RULE"]["HNT_SPACE"]
            if len(t_space_standby) != 0 and dumper == recognize_separator:
                tokenized.append(t_space_standby_token_name)
                tokenized.append("HNT_SPACE")
                dumper = ""
                t_space_standby_token_name = ""
                t_space_standby = ""
                t_suggest = {}
            elif len(t_space_standby) != 0:
                user_string = list(t_space_standby)
                t_space_standby = ""
                t_space_standby_token_name = ""
                dumper = ""
                t_suggest = {}
                for token_meaningful_user_string in user_string:
                    tokenized.append("HNT_MEANINGFUL_USER_STRING_"+token_meaningful_user_string)
                    tokenized.append(recognize_separator)
            elif len(t_suggest) != 0:
                for t_suggest_name, t_suggest_real in t_suggest.items():
                    if t_suggest_real == dumper:
                        t_space_standby_token_name = t_suggest_name
                        t_space_standby = t_suggest_real
                        dumper = ""
                    elif not t_suggest_real.startswith(dumper):
                        t_suggest.pop(t_suggest_name)
                if len(t_suggest) == 0:
                    user_string = list(dumper)
                    dumper = ""
                    for token_meaningful_user_string in user_string:
                        tokenized.append("HNT_MEANINGFUL_USER_STRING_"+token_meaningful_user_string)
            else:
                token_processed = False
                token_insert_suggested = False
                for t_member in tokens.values():
                    for t_name, t_real in t_member.items():
                        if dumper == t_real:
                            tokenized.append(t_name)
                            dumper = ""
                            token_processed = True
                            break
                        elif t_real.startswith(dumper):
                            t_suggest[t_name] = t_real
                            token_insert_suggested = True
                    if token_processed:
                        break
                if not token_processed and not token_insert_suggested:
                    tokenized.append("HNT_MEANINGFUL_USER_STRING_"+dumper)
                    dumper = ""
        return tokenized

    def token_debug(self):
        tokens = self.token()
        for t_group, t_member in tokens.items():
            print(t_group, "===>")
            for t_name, t_real in t_member.items():
                print("    ", t_real, "===>", t_name)


    def token(self):
        return {
            "HNT_SYNTAX_TOKEN": {
                "HNT_SYNTAX_IF": "if",
                "HNT_SYNTAX_ELSE": "else",
                "HNT_SYNTAX_IFELSE": "ifelse",
                "HNT_SYNTAX_IFEL": "ifel",
                "HNT_SYNTAX_LOOP":"loop",
                "HNT_SYNTAX_SEE": "see",
                "HNT_SYNTAX_ISSUE": "issue"
            },
            "HNT_OPERATOR_TOKEN": {
                "HNT_ADD": "+",
                "HNT_SUB": "-",
                "HNT_MULT": "*",
                "HNT_DIVI": "/",
                "HNT_REMA": "%"
            },
            "HNT_SUPPLEMENT_TOKEN": {
                "HNT_CONNOTATION": "cnot",
                "HNT_LOCK": "lock",
                "HNT_VAR_DECLARE": "decl",
                "HNT_FUNCTION_DECLARE": "fn",
                "HNT_CLASS_DECLARE": "cls"
            },
            "HNT_TYPE_TOKEN": {
                "HNT_STRING": "str",
                "HNT_INTEGER": "integer",
                "HNT_BOOLEAN": "bool",
                "HNT_FLOAT": "float",
                "HNT_BYTE": "byte",
                "HN_FN_RETURN_REFERENCE": "ref_fn",
            },
            "HNT_MEANINGFUL_TOKEN": {
                "HNT_BLOCK_START": "{",
                "HNT_BLOCK_END": "}",
                "HNT_ASSIGNMENT": "=",
                "HNT_EQ": "==",
                "HNT_REVERSAL_RESULT": "!",
                "HNT_TYPE_EXPLANATION": "->",
                "HNT_METHOD_CALL": "=>",
                "HNT_ANY_TYPE_EXPLANATION": "|",
                "HNT_FN_CLS_ARGUMENT_START": "(",
                "HNT_FN_CLS_ARGUMENT_END": ")",
                "HNT_LIST_START": "[",
                "HNT_LIST_END": "]",
                "HNT_STRING_SINGLE_QUOTE": "'",
                "HNT_STRING_DOUBLE_QUOTE": '"',
                "HNT_TYPE_EQ": "?",
                "HNT_CONCURRENTLY": "&",
                "HNT_WHICH_ONE": "||",
                "HNT_END_CODE": ";",
                "HNT_GREATER_THAN": ">",
                "HNT_LESS_THAN": ">",
                "HNT_LESS_THAN_OR_EQUAL_TO": "=<",
                "HNT_GREATER_THAN_OR_EQUAL_TO": ">=",
                "HNT_PIPELINE": "|>"
            },
            "HNT_READABILITY_RULE": {
                "HNT_NEWLINE": "\n",
                "HNT_NEWLINE_CRLF": "\r\n",
                "HNT_SPACE": " ",
                "HNT_TAB": "\t"
            },
        }