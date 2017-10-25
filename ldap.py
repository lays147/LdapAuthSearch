import ldap
try:
    ldap_conn = ldap.initialize("ldap://192.168.0.1")
    ldap_conn.protocol_version = ldap.VERSION3
    ldap_conn.set_option(ldap.OPT_REFERRALS, 0)
    ldap_conn.simple_bind_s("user@domain", "pwd")
    print("Authentication was a success!")
    base_domain = "dc=domain"
    retrieveAttributes = ["memberOf"]
    searchFilter = "(&(objectCategory=group))"
    print("Starting search!")
    result = ldap_conn.search_s(
        base_domain,
        ldap.SCOPE_SUBTREE,
        searchFilter,
        retrieveAttributes)
    print("Search result: ")
    print (result)
    l.unbind_s()
except ldap.LDAPError as e:
    print("Ops! An exeption happened!")
    print(e)
    l.unbind_s()
