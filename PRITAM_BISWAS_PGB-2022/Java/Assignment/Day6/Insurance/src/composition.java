import java.util.*;

class insaurance {

    public String policy_no;

    public String policy_name;

    insaurance(String policy_no, String policy_name)

    {

        this.policy_no = policy_no;

        this.policy_name = policy_name;

    }


}

class Record {

    private final List<insaurance> insaurance;

    Record(List<insaurance> insaurance)

    {

        this.insaurance = insaurance;

    }

    public List<insaurance> getListOfInsauranceInRecord()

    {

        return insaurance;

    }

}

class composition {

    public static void main(String[] args)

    {

        insaurance b1

            = new insaurance("2342", "	Health Insaurance");

        insaurance b2

            = new insaurance("5632", "Life Insaurance");

        insaurance b3 = new insaurance("7823",

                           "Life Insaurance");

        List<insaurance> insaurance = new ArrayList<insaurance>();

        insaurance.add(b1);

        insaurance.add(b2);

        insaurance.add(b3);

        Record Record = new Record(insaurance);

        List<insaurance> insaurances

            = Record.getListOfInsauranceInRecord();

        for (insaurance bk : insaurances) {

            System.out.println("POlicy_no : " + bk.policy_no

                               + " and "

                               + " Policy name : " + bk.policy_name);

        }

    }

}