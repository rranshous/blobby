namespace blobby

/*
simple blob server
*/

/* Simple exception type */
exception Exception
{
    1: string msg
}

/* content based blob server, the keys are the hashes */
service Blobby {
    // returns the data
    string get (1: string bhash)
    throws (1: Exception ex);

    // returns the bhash 
    string set (1: string data)
    throws (1: Exception ex);

    // deletes the data
    bool delete (1: string bhash)
    throws (1: Exception ex);
}
