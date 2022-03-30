package task1;
import java.util.*;

class penclass {

    public String type;

    public String brand;

    penclass(String type, String brand)

    {

        this.type = type;

        this.brand = brand;

    }

}

class penstore {

    private final List<penclass> pens;

    penstore(List<penclass> pens)

    {

        this.pens = pens;

    }

    public List<penclass> getListOfpens()

    {

        return pens;

    }

}

class composition {

    public static void main(String[] args)

    {

        penclass p1

            = new penclass("ink pen", "cello");

        penclass p2

            = new penclass("ball point pen", "parker");

        penclass p3 = new penclass("ball point pen",

                           "camlin");

        List<penclass> penclass = new ArrayList<penclass>();

        penclass.add(p1);

        penclass.add(p2);

        penclass.add(p3);

        penstore penobj = new penstore(penclass);

        List<penclass> pens

            = penobj.getListOfpens();

        for (penclass ps : pens) {

            System.out.println("Type : " + ps.type

                               + " and "

                               + " Brand : " + ps.brand);

        }

    }

} 