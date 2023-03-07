// See https://aka.ms/new-console-template for more information
using System.ComponentModel.DataAnnotations;
using System.Runtime.InteropServices;

//Console.WriteLine("Hello, World!");
//var nimi = Console.ReadLine();
//if (nimi.ToUpper()=="JUKU")
//{
//    Console.WriteLine("Lahme kinno");
//    int vanus = Convert.ToInt32(Console.ReadLine());
//    if (vanus<0 || vanus>120) // &&- and, ||- or
//    {
//        Console.WriteLine("Vanus ei saa {vanus} olla", vanus);
//    }
//    else if (vanus<6)
//    {
//        Console.WriteLine("Sulle on pilet tasuta!", vanus); 
//    }
//    else if (vanus>=6 && vanus<=14)
//    {
//        Console.WriteLine("Sulle tuleb osta lastepilet", vanus);
//    }
//    else if (vanus>=15 && vanus<=65)
//    {
//        Console.WriteLine("Sulle tuleb osta täispilet", vanus);
//    }
//    else if (vanus>65)
//    {
//        Console.WriteLine("Sulle tuleb osta sooduspilet", vanus);
//    }
//}
//else
//{
//    Console.WriteLine("Mind kodus pole");
//}
//Console.Clear(); // чистит консоль
////изменение визуала
//Console.BackgroundColor = ConsoleColor.Magenta;
//Console.ForegroundColor = ConsoleColor.Yellow;

Random rnd = new Random();
//int hinne = rnd.Next(1, 5);
//Console.WriteLine("Täna said hinne {0}", hinne);
//string reaktsioon = "";
//switch (hinne)
//{
//    case 1: reaktsioon = "Õpi veel!"; break;
//    case 2: reaktsioon = "Õpi natuke veel!"; break;
//    case 3: reaktsioon = "Rahuldav!"; break;
//    case 4: reaktsioon = "Hea tulemus!"; break;
//    case 5: reaktsioon = "Väga hea!"; break;
//    default:
//        reaktsioon = "Viga!";
//        break;
//}
//Console.WriteLine("for abil");
//for (int i = 0; i < hinne; i++) ;
//{
//    Console.WriteLine(reaktsioon);
//}
//Console.WriteLine("while abil");
//int hinne_test = hinne;
//while (hinne > 0)
//{
//    hinne--;
//    Console.WriteLine(reaktsioon);
//}
//Console.WriteLine("do while abil");
//do
//{
//    Console.WriteLine(reaktsioon);
//    hinne_test--;
//} while (hinne_test != 0);
//Console.Clear();
//var komm = "";
//do
//{
//    Console.Clear();
//    Console.WriteLine("Tahan kommi!");
//    komm = Console.ReadLine();
//} while (komm != "Komm");

//while (komm != "Komm")
//{
//    Console.Beep();
//    Console.Clear();
//    Console.WriteLine("Tahan kommi!");
//    komm = Console.ReadLine();
//}
//Console.WriteLine("Tere, " + nimi);
//Console.WriteLine("Arv 1: ");
//int arv1 = int.Parse(Console.ReadLine());
//Console.WriteLine("Arv 2: ");
//int arv2 = int.Parse(Console.ReadLine());
//Console.WriteLine("Tehe: ");
//char tehe = Convert.ToChar(Console.ReadLine()[0]);
//double vastus = 0;
//if (tehe == '+')
//{
//    double vastus = arv1 + arv2;
//}
//else if (tehe == '-')
//{
//    double vastus = arv1 - arv2;
//}
//else if (tehe == '/')
//{
//    double vastus = arv1 / arv2;
//}
//else
//{
//    Console.WriteLine("{0} - tundmatu tehe", tehe);
//}
//Console.WriteLine("Arvude {0} ja {1} korrutis võrdub {2}", arv1,arv2,vastus);

int kogus = rnd.Next(1, 10);
string[] Nimed = new string[kogus];

for (int i = 0; i < kogus; i++)
{
    Console.WriteLine("Sisesta {0}. nimi: ", i + 1);
    Nimed[i] = Console.ReadLine();
    
}

for (int i = 0; i < Nimed.Length; i++)
{
    Console.WriteLine("Tere {0}", Nimed[i]);
}

//Mis arv mõtles välja arvuti? Kasuta vähemalt 5 katset, et seda teada. 
int katse = 0;
int arvuti = rnd.Next(1, 100);
int inimene;
do
{
    inimene = Convert.ToInt32(Console.ReadLine());
    katse++;
} while (inimene!=arvuti || katse!=5);

//Korrutustabel väljata ekraanile sellisel kujul:
for (int i = 0; i < 11; i++)
{
    for (int j = 0; j < 11; j++)
    {
        Console.Write("{0,4}", i * j);
    }
    Console.WriteLine();
}

int[] Arvud = new int[5];
for (int i = 0; i < 5; i++)
{
    Arvud[i] = Convert.ToInt32(Console.ReadLine());    
}
int summa=0, korrutis=1;
double keskmine;

foreach (int arv in Arvud)
{
    Console.Write("{0,5}", arv);
    summa = summa + arv;
    korrutis = korrutis * arv;
}
Console.WriteLine();
keskmine = summa / Arvud.Length;
Console.WriteLine("Summa={0},\nKorrutis={1},\nKeskmine={2}", summa, korrutis, keskmine);